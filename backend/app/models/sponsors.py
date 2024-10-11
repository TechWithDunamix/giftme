
from .bases import C_BaseModels

from django.db import models
from random import shuffle

from datetime import datetime,timedelta

from django.utils import timezone

from django.db import transaction
class Sponsors(C_BaseModels):

    email :str = models.EmailField(unique=True)

    otp :str = models.CharField(max_length=12)

    otp_created :models.DateField = models.DateField(auto_now_add=True)

    username :str = models.CharField(max_length=120, unique=True)
    class Meta:
        db_table = "Sponsors"

    
    def generate_otp(self):
        nums :list = [x for x in range(0,10)]
        shuffle(nums)
        return "".join(str(x) for x in nums[:6])
    
    @transaction.atomic
    def save(self, **kwargs):

        return super().save(**kwargs)
    

   
    @classmethod
    def get_or_create(cls, **kwargs : dict):
        email :str = kwargs.get("email")

        _obj  = cls.objects.filter(email = email)
        if _obj.exists():

            if  _obj.first().date_created + timedelta(minutes=90) < timezone.now():
                obj = _obj.first()
                
                obj.username = obj.email.split("@")[0]
                obj.otp = obj.generate_otp()
                obj.date_created = timezone.now()
                obj.save()
                
                return obj
            
            

            return _obj.first()
        
        return cls.objects.create(email = email)
            

        

        


            
    
