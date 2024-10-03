from django.db import models 
import uuid
from datetime import datetime
class C_BaseModels(models.Model):
    id: uuid.UUID = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)

    date_created:datetime = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        abstract = True