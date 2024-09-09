from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = "apps"

    def ready(self):
        # Makes sure all signal handlers are connected
        from apps import handlers # noqa