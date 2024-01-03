from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'realsite'

    def ready(self):
        import realsite.signals

class RealsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'realsite'
