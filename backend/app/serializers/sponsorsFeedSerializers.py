from rest_framework import serializers
from ..models import UserPost ,AuthUserModel,ProductList,Category,UserProfile
from django.http import HttpRequest
from typing import Dict,List
class SponsorsPostFeedListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserPost

        fields = ["id","title","date_created","id","exlusive", "image", "user"]


    def get_image(self,instance :UserPost):
        request :HttpRequest = self.context.get("request")
        image = instance.get_image_list()[0]
        return request.build_absolute_uri(image.image) if image.image else ""

    def get_user(self, instance :UserPost):
        request :HttpRequest = self.context.get("request")

        user_data = {
            "username" : instance.user.username,
            "id" :  instance.user.id,
            "profile_image" : request.build_absolute_uri(instance.user.user_profile.profile_image) if instance.user.user_profile.profile_image else ""
        }

        return user_data
    

class ProductsFeedsListSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    user = serializers.SerializerMethodField()

    name :str = serializers.CharField()

    description:str = serializers.CharField()

    price :float = serializers.FloatField()

    categories :List = serializers.SerializerMethodField()

    image :str = serializers.SerializerMethodField()

    def get_user(self, instance :ProductList) -> Dict[str, str]:
        request :HttpRequest = self.context.get("request")
        user :List[AuthUserModel,UserProfile] = [instance.user, instance.user.user_profile]    
        return {
            "username" : user[0].username,
            "profile_image" : request.build_absolute_uri(user[1].profile_image.url) if user[1].profile_image else None,
            "cover_image" : request.build_absolute_uri(user[1].cover_image.url) if user[1].cover_image else None,
               
        }
    def get_categories(self, instance :ProductList ):
        return [x.name for x in instance.category.all()]
    
    def get_image(self,instance :ProductList):
        request :HttpRequest = self.context.get("request")
        return request.build_absolute_uri(instance.image.url)

