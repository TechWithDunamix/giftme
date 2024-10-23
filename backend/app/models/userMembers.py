from .bases import C_BaseModels 
from .authModels import AuthUserModel
from .sponsors import Sponsors
from django.db import models
from .userMemberships import UserMembership
import datetime
from django.db import transaction
class UserMembers(C_BaseModels):
    sponsor = models.ForeignKey(Sponsors,on_delete=models.CASCADE,related_name="memberhips")

    user = models.ForeignKey(AuthUserModel,on_delete=models.CASCADE,related_name="members")

    membershiPlan = models.ForeignKey(UserMembership,on_delete = models.CASCADE,related_name="sponsor_members")

    yearly = models.BooleanField(default = False)

    date_due = models.DateTimeField(blank=True, null = True)
    


    class Meta:
        db_table = "User  Members"


    @transaction.atomic
    def save(self, **kwargs : dict):
        self.date_due = datetime.datetime.utcnow() + datetime.timedelta(days=30)

        if self.yearly:
            self.date_due = datetime.datetime.utcnow() + datetime.timedelta(days=365)

        return super(UserMembers).save(**kwargs)



    