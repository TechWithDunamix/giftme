from .authModels import AuthUserModel 
from typing import Iterable, Union,Optional
from django.db import models
from django.db import transaction

import uuid 

class UserProfile(models.Model):

    id:uuid.UUID = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)

    user:Union[AuthUserModel,object] = models.OneToOneField(AuthUserModel,
                                                        related_name="user_profile",    
                                                        on_delete=models.CASCADE)
    
    bio:str = models.TextField()
    interests:list = models.JSONField(default=list,null=True)

    profile_image:models.ImageField = models.ImageField(upload_to="user_profile",null=True)

    cover_image:models.ImageField = models.ImageField(upload_to="cover_images",null=True)

    socials:list = models.JSONField(default=list,null=True)

    paymentDetails =models.JSONField(default=dict,null=True)
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    

    def save(self, **kwargs:dict) -> None:
        with transaction.atomic():
            return super().save(**kwargs)
        

    @property
    def username(self):
        return self.user.username 
    
    
    


    class Meta:
        db_table = "User Profile"