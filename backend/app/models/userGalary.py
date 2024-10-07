from typing import Iterable
from django.db import models,transaction
from .bases import C_BaseModels 
from .imageSchema import Images
from .authModels import AuthUserModel
class UserGalary(C_BaseModels):

    user :AuthUserModel = models.ForeignKey(AuthUserModel,related_name="user_galaries",on_delete=models.CASCADE)

    title :str = models.CharField(max_length=120)

    images :Images = models.ManyToManyField(Images,related_name="user_galaries")

    exclusive :bool = models.BooleanField(default=False)

    description :str = models.TextField()


    def __str__(self) -> str:
        return f'{self.user.username} Galary'
    


    @transaction.atomic
    def save(self,**kwargs) -> None:

        return super().save(**kwargs)
    
    def get_image_list(self):
        return self.images.all()
    

    class Meta:
        db_table = "User Galary"