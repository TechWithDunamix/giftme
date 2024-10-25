from typing import Iterable
from .bases import C_BaseModels
from django.db import models
from uuid import UUID
from django.db import transaction
from django.apps import apps
# from django.apps import 
class Reaction(C_BaseModels):
    object_id :UUID = models.UUIDField()

    email :str = models.EmailField()

    reaction :str = models.CharField(max_length=120)

    object_name :str = models.CharField(max_length=220)

    


    @transaction.atomic
    def save(self, **kwargs):
        try:
            model_name = apps.get_model(app_label="app", model_name=self.object_name)
        except LookupError:
            raise NotImplemented("Model does not exist")
        return super().save(**kwargs)




