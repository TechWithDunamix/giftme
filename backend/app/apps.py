from django.apps import AppConfig
import os 

class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"


    def ready(self) -> None:
        from . import models

