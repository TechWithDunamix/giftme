from typing import Iterable
from .bases import C_BaseModels
from .authModels import AuthUserModel   
from django.db import models
from uuid import uuid4
from django.db import transaction

class Images(C_BaseModels):
    user :AuthUserModel = models.ForeignKey(AuthUserModel,related_name="user_images",on_delete=models.CASCADE)

    image :models.ImageField = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return f'file[{self.image.name}] by {self.user.username} on {self.date_created}'



    class Meta:
        db_table = "User Images"


    @transaction.atomic
    def save(self, **kwargs) -> None:
        self.image.name = f'{uuid4()}.png'
        return super().save(**kwargs)
    
    @transaction.atomic
    def delete(self,**kwargs) -> tuple[int, dict[str, int]]:
        if self.image:
            self.image.delete()
        return super().delete(**kwargs)