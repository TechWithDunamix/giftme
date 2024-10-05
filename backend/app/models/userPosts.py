from .bases import C_BaseModels 
from django.db import models
from .authModels import AuthUserModel
from .imageSchema import Images
from django.utils import timezone
from ..common.managers import PostManager
from django.db.models import Manager

class UserPost(C_BaseModels):

    user :AuthUserModel = models.ForeignKey(AuthUserModel,on_delete=models.CASCADE,related_name="user_post")

    title :str = models.CharField(max_length=250)

    body :str  = models.TextField()

    images = models.ManyToManyField(Images,related_name="get_post")

    scheduled :bool = models.BooleanField(default = False)

    scheduled_for = models.DateTimeField(null = True,default=timezone.now)

    draft :bool = models.BooleanField(default = False)

    exlusive :bool = models.BooleanField(default=False)

    objects :Manager = PostManager()

    class Meta:
        db_table = "User Post"



    def get_image_list(self) -> list:
        return self.images.all()
    
