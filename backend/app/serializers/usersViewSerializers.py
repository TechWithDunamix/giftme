from ..models.authModels import AuthUserModel 
from rest_framework import serializers
from django.http import HttpRequest
from ..models.userFollowerShip import Followership
from ..models.userMembers import UserMembers
from django.db import models
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
    


class UserDetailViewSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    cover_image = serializers.SerializerMethodField()

    bio = serializers.SerializerMethodField()

    interests  = serializers.SerializerMethodField()

    socials = serializers.SerializerMethodField()

    followers = serializers.SerializerMethodField()

    members = serializers.SerializerMethodField()

    is_following = serializers.SerializerMethodField()

    is_member = serializers.SerializerMethodField()


    class Meta:
        model = AuthUserModel

        fields = ["id", "username", "cover_image", 
                  "profile_image","bio","interests","socials",
                  "followers","members","is_following","is_member"]
        

    def get_cover_image(self, instance:AuthUserModel):
        request :HttpRequest = self.context.get("request")
        return request.build_absolute_uri(instance.user_profile.cover_image.url) if instance.user_profile.cover_image else None
    


    def get_profile_image(self, instance:AuthUserModel):
        request :HttpRequest = self.context.get("request")
        return request.build_absolute_uri(instance.user_profile.profile_image.url) if instance.user_profile.profile_image else None
    

    def get_bio(self, instance:AuthUserModel):
      return instance.user_profile.bio
    
    def get_socials(self, instance:AuthUserModel):
      return instance.user_profile.socials
    
    def get_interests(self, instance:AuthUserModel):
      return instance.user_profile.interests
    
    def get_followers(self, instance):
       return len(Followership.objects.filter(user = instance))
    
    def get_members(self, instance):
       return len(UserMembers.objects.filter(user = instance))
    
    def get_is_following(self, instance):
       request :HttpRequest = self.context.get("request")
       if request.user.is_anonymous:
          return False
       
       # Below : i had to use 'sponsor__email' so i can validate both bth user and sponsors 
       query = models.Q(user = instance) & models.Q(sponsor__email = request.user.email)


       if Followership.objects.filter(query).exists():
          return True
       return False
    
    def get_is_member(self, instance):
       request :HttpRequest = self.context.get("request")
       if request.user.is_anonymous:
          return False
       
       # Below : i had to use 'sponsor__email' so i can validate both bth user and sponsors 
       query = models.Q(user = instance) & models.Q(sponsor__email = request.user.email)


       if UserMembers.objects.filter(query).exists():
          return True
       return False