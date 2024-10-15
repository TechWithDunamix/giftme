from .authModels import AuthUserModel 
from.sponsors import Sponsors
from .bases import C_BaseModels
from django.db import models 


class Followership(C_BaseModels):

    user = models.ForeignKey(AuthUserModel,related_name="followers",on_delete=models.CASCADE)

    sponsors = models.ForeignKey(Sponsors,on_delete=models.CASCADE,related_name="following")

    