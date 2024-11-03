from django.db import models
from django.contrib.auth.models import AbstractBaseUser 

from datetime import datetime
from typing import Iterable, Union,Optional
from ..common.validators import AuthValidators
from ..common.managers import UserManager
from django.db import transaction
from .comments import Comment
from django.db.models import F,FloatField,ExpressionWrapper,Count
import uuid
USER_CREATION_VALIDATORS = AuthValidators()
class AuthUserModel(AbstractBaseUser):

    objects = UserManager()


    id:uuid.UUID = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    email:str = models.EmailField(unique=True)

    first_name:str = models.CharField(max_length=125,
                                      validators=[
                                          USER_CREATION_VALIDATORS.validate_first_name
                                          ])

    last_name:str = models.CharField(max_length=120, validators=[
                                          USER_CREATION_VALIDATORS.validate_last_name
                                          ])

    username:Optional[str] = models.CharField(max_length=120,unique=True)

    date_created:Union[str,datetime] = models.DateTimeField(auto_now_add=True)

    last_updated:Union[str,datetime] = models.DateTimeField(auto_now_add=True)


    country:str = models.CharField(max_length=230,default="Nigeria")

    is_active:bool = models.BooleanField(default=True)

    USERNAME_FIELD:str = "email"

    account_id :str = models.CharField(max_length=160, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

    def save(self,**kwargs: str) -> None:
        # if self.objects.filter(username = self.username).exists():
        #     self.username:str = f"${self.username}${crypto.get_random_string(4)}"
        with transaction.atomic():
            return super().save(**kwargs)
        

    
    
    @classmethod
    def get_top_users(cls, top_n = 10):
        return cls.objects.annotate(
            memberships__count = Count("memberships"),
            user_products__count = Count("user_products"),
            followers__count = Count("followers")
            ,weighted_score = ExpressionWrapper(
            F('memberships__count') * 0.5 +
            F('user_products__count') * 0.1 +
            F('followers__count') * 0.2 +
            Comment.objects.filter(
                models.Q(object_id=F('id')) &
                models.Q(object_name=cls.__name__)
            ).count() * 0.2,
            output_field=FloatField()
        )).order_by("-weighted_score")


    
    class Meta:
        db_table:str = 'Users'
        app_label:str = "app"



