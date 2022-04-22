import logging
import os
from django_rest_passwordreset.signals import reset_password_token_created
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver
from django.urls import reverse
from mediusware_coding_test.core import email_threading as email_threading_core


logger = logging.getLogger(__name__)


User = get_user_model()


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """

    # send an e-mail to the user
    context = {
        "current_user": reset_password_token.user,
        "username": reset_password_token.user.username,
        "email": reset_password_token.user.email,
        "reset_password_url": instance.request.build_absolute_uri(
            reverse(
                "core:password-reset-confirm",
                kwargs={"token": reset_password_token.key},
            )
        ),
    }
    logger.info(reset_password_token.user.email)

    logger.info(context)

    email_threading_core.send_html_mail(
        "Mediusware Password Reset",
        context,
        "registration/password_reset_email.html",
        "mdfaisalnstu@gmail.com",
        reset_password_token.user.email,
    )
