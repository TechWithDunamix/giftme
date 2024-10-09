from rest_framework import serializers 
from ..models.userProfile import UserProfile 
from ..models.authModels import AuthUserModel
from typing import Any
from .bases import MainUserDataSerializer
from django.http import HttpRequest
class UserProfileCreationSerializer(serializers.Serializer):
    bio:str = serializers.CharField(required = True)

    interests:list = serializers.ListField(
        child = serializers.CharField(required = False),
        required = False
    )

    profile_image:Any = serializers.ImageField(required = False)
    cover_image:Any = serializers.ImageField(required = False)

    socials:list = serializers.ListField(
        child = serializers.CharField(required = False),
        required = False
    )



class UserProfileViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile  

        fields = "__all__"
    def to_representation(self, instance):

        data:dict = super().to_representation(instance)
        request:HttpRequest = self.context.get("request")
        if  request:
            
            profile_image :str =   request.build_absolute_uri(instance.profile_image.url)
            cover_image :str =   request.build_absolute_uri(instance.cover_image.url)

            data.setdefault("profile_image",profile_image)
            data.setdefault("cover_image",cover_image)
    
        user_data = MainUserDataSerializer(instance.user).data
        
        return {**data,**user_data}



class UserProfileUpdateSerializer(serializers.Serializer):
    email  :str = serializers.EmailField(required = False)
    first_name:str = serializers.CharField(required = False)
    last_name :str = serializers.CharField(required = False)
    bio:str = serializers.CharField(required = False)

    interests:list = serializers.ListField(
        child = serializers.CharField(required = False),
        required = False
    )

    profile_image:Any = serializers.ImageField(required = False)
    cover_image  :Any = serializers.ImageField(required = False)

    socials  :list = serializers.ListField(
        child = serializers.CharField(required = False),
        required = False
    )


    username  :str = serializers.CharField(required = False)

    paymentDetails :str =serializers.JSONField(required = False)


    def validate_email(self, value :str) -> str:
        request :HttpRequest = self.context.get("request")
        if AuthUserModel.objects.exclude(email = request.user.email).filter(email = value).exists():
            raise serializers.ValidationError("User with this email already exists .")
        
        return value
    

    def validate_username(self, value :str) -> str:
        request :HttpRequest = self.context.get("request")
        
        if AuthUserModel.objects.exclude(username = request.user.username).filter(username = value).exists():
            raise serializers.ValidationError("User with this username already exists .")
        
        return value





    


   