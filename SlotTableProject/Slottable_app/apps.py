from django.apps import AppConfig


class SlottableAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Slottable_app'
