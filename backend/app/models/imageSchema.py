from .bases import C_BaseModels
from .authModels import AuthUserModel   
from django.db import models

class Images(C_BaseModels):
    user :AuthUserModel = models.ForeignKey(AuthUserModel,related_name="user_images",on_delete=models.CASCADE)

    image :models.ImageField = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return f'file[{self.image.name}] by {self.user.username} on {self.date_created}'



    class Meta:
        db_table = "User Images"