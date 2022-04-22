from rest_framework import serializers
from django.contrib.auth import get_user_model
from mediusware_coding_test.apps.user import models as models_user
from mediusware_coding_test.core.api.serializers import DynamicFieldsModelSerializer
from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from mediusware_coding_test.apps.user import validators as user_validators
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class UserProfileSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(required=False)
    is_sys_admin_user = serializers.SerializerMethodField()

    class Meta:
        model = models_user.User
        fields = [
            "id",
            "username",
            "name",
            "timezone",
            "timestamp_format",
            "is_sys_admin_user",
        ]

    def get_is_sys_admin_user(self, obj):
        if obj.user_type == models_user.User.UserTypes.SYS_ADMIN:
            return True
        return False


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User

    def validate(self, attrs):
        new_password = attrs.get("new_password")

        # validate with django default validate_password
        django_validate_password(new_password)

        # password complexity validator
        errors, contain_space = user_validators.password_complexity_validator(
            new_password
        )

        if errors:
            raise serializers.ValidationError(
                _(f"Password: Must be more strong (must contain {', '.join(errors)})")
            )

        if contain_space:
            raise serializers.ValidationError(
                _("Password: Can't contain space"))

        return super().validate(attrs)
