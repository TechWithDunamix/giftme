from .bases import C_BaseModels 
from .authModels import AuthUserModel
from .sponsors import Sponsors
from django.db import models
from .userMemberships import UserMembership
class UserMembers(C_BaseModels):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE,related_name="memberhips")

    user = models.ForeignKey(AuthUserModel,on_delete=models.CASCADE,related_name="members")

    membershiPlan = models.ForeignKey(UserMembership,on_delete = models.CASCADE,related_name="sponsor_members")


    class Meta:
        db_table = "User  Members"

        

    


