from .bases import C_BaseModels 
from django.db import models
from typing import Iterable, Union
from .authModels import AuthUserModel
from django.db import transaction
class UserMembership(C_BaseModels) :

    user = models.ForeignKey(AuthUserModel,on_delete=models.CASCADE,related_name="memberships",null = True)

    name :str = models.CharField(max_length=225)

    image :models.ImageField = models.ImageField(null=True,upload_to="memberships_images")

    rewards :list = models.JSONField(default=list)

    welcome_note :str = models.TextField(null=True)

    description :str = models.TextField()

    price_per_month :float = models.FloatField()

    price_per_year :float = models.FloatField(null=True) 

    full_time :bool = models.BooleanField(default=False)

    max_members :int = models.IntegerField(null=True,default=1000)

    limit_members :bool = models.BooleanField(default=False)

    full_price :float = models.IntegerField(null=True)

    

    @property
    def get_prices(self) -> Union[list | int]:

        if self.full_time:
            return self.full_price
        
        return [self.price_per_month,self.price_per_year]



    @property
    def maxed_out(self):
        return True if self.limit_members else False
        

    class Meta:
        db_table = "User Membership !"


    @transaction.atomic
    def save(self, **kwargs):
        return super().save(**kwargs)
    
    @transaction.atomic
    def delete(self, **kwargs):
        self.image.delete()
        return super().delete(**kwargs)
    