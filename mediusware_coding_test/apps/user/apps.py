from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'mediusware_coding_test.apps.user'

    def ready(self):
        import mediusware_coding_test.apps.user.signals
