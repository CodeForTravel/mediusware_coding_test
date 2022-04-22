import pytz
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import MinValueValidator
from mediusware_coding_test.core import utils as utils_core


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=255,
        unique=True,
        help_text=_(
            "Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    name = models.CharField(_("Name"), blank=True, max_length=255)

    is_weak_password = models.BooleanField(default=False)
    weak_password_attempt = models.IntegerField(
        validators=[MinValueValidator(0)], default=3
    )

    class UserTypes(models.IntegerChoices):
        SYS_ADMIN = 1, _("System Admin")

    user_type = models.IntegerField(
        _("Type"), choices=UserTypes.choices, null=True, blank=True)

    TIMEZONE_CHOICES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    TIMEZONE_KL = utils_core.get_pytz_timezone(settings.TIME_ZONE_KL)

    timezone = models.CharField(
        _("Time Zone"),
        max_length=50,
        choices=TIMEZONE_CHOICES,
        default=settings.TIME_ZONE_KL,
    )

    class TimestampChoices(models.TextChoices):
        FORMAT_DDMMYYYY_24HOUR = "%d/%m/%Y | %H:%M:%S", "dd/mm/yyyy | HH:mm:ss"
        FORMAT_DDMMYYYY_12HOUR = "%d/%m/%Y | %I:%M:%S %p", "dd/mm/yyyy | HH:mm:ss AM/PM"
        FORMAT_24HOUR_DDMMYYYY = "%H:%M:%S | %d/%m/%Y", "HH:mm:ss | dd/mm/yyyy"
        FORMAT_12HOUR_DDMMYYYY = (
            "%I:%M:%S %p | %d/%m/%Y",
            "HH:mm:ss AM/PM |  dd/mm/yyyy",
        )
        FORMAT_MMDDYYYY_24HOUR = "%m/%d/%Y | %H:%M:%S", "mm/dd/yyyy | HH:mm:ss"
        FORMAT_MMDDYYYY_12HOUR = "%m/%d/%Y | %I:%M:%S %p", "mm/dd/yyyy | HH:mm:ss AM/PM"
        FORMAT_24HOUR_MMDDYYYY = "%H:%M:%S | %m/%d/%Y", "HH:mm:ss | mm/dd/yyyy"
        FORMAT_12HOUR_MMDDYYYY = "%I:%M:%S %p | %m/%d/%Y", "HH:mm:ss AM/PM | mm/dd/yyyy"
        FORMAT_YYYYMMDD_24HOUR = "%Y/%m/%d | %H:%M:%S", "yyyy/mm/dd | HH:mm:ss"
        FORMAT_YYYYMMDD_12HOUR = "%Y/%m/%d | %I:%M:%S %p", "yyyy/mm/dd | HH:mm:ss AM/PM"
        FORMAT_24HOUR_YYYYMMDD = "%H:%M:%S | %Y/%m/%d", "HH:mm:ss | yyyy/mm/dd"
        FORMAT_12HOUR_YYYYMMDD = "%I:%M:%S %p | %Y/%m/%d", "HH:mm:ss AM/PM | yyyy/mm/dd"

    timestamp_format = models.CharField(
        _("Timestamp Format"),
        max_length=22,
        choices=TimestampChoices.choices,
        default=TimestampChoices.FORMAT_DDMMYYYY_24HOUR,
    )

    @property
    def is_sysadmin(self):
        if self.user_type == self.UserTypes.SYS_ADMIN:
            return True
        return False

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})


class SysAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.UserTypes.SYS_ADMIN)


class SysAdmin(User):
    objects = SysAdminManager()

    class Meta:
        proxy = True
