from .authModels import AuthUserModel
from .sponsors import Sponsors
from .bases import C_BaseModels
from django.db import models


class Payments(C_BaseModels):

    object_id = models.UUIDField(null=True)

    user = models.ForeignKey(AuthUserModel, related_name="user_payments",on_delete = models.CASCADE)

    verified :bool = models.BooleanField(default=False)

    sponsor = models.ForeignKey(Sponsors, on_delete = models.CASCADE, related_name="payments")

    amount :float = models.FloatField()

    message = models.TextField(null=True)

    refrence :str = models.CharField()

    object_name :str = models.CharField()

    class Meta:

        db_table = "User Payment"


