
from .bases import C_BaseModels

from django.db import models

# from django.utils.crypto import get_random_string

class Sponsors(C_BaseModels):

    email :str = models.EmailField(unique=True)

    otp :str = models.CharField(max_length=12)

    otp_created :models.DateField = models.DateField(auto_created=True)

    username :str = models.CharField(max_length=120, unique=True)
    class Meta:
        db_table = "Sponsors"

    

    def save(self, **kwargs):
        nums :list = [x for x in range(0,10)]

        self.otp = "".join(str(x) for x in nums[:6])
        return super().save(**kwargs)