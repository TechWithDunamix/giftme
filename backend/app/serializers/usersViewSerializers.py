from ..models.authModels import AuthUserModel 
from rest_framework import serializers
from django.http import HttpRequest
class UserListViewSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    cover_image = serializers.SerializerMethodField()

    bio = serializers.SerializerMethodField()
    

    class Meta:
        model = AuthUserModel 

        fields = ["id", "username", "cover_image", "profile_image","bio"]

    def get_cover_image(self, instance:AuthUserModel):
        request :HttpRequest = self.context.get("request")
        return request.build_absolute_uri(instance.user_profile.cover_image.url) if instance.user_profile.cover_image else None
    


    def get_profile_image(self, instance:AuthUserModel):
        request :HttpRequest = self.context.get("request")
        return request.build_absolute_uri(instance.user_profile.profile_image.url) if instance.user_profile.profile_image else None
    

    def get_bio(self, instance:AuthUserModel):
      return instance.user_profile.bio