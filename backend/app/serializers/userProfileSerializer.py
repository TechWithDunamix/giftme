from rest_framework import serializers 
from ..models.userProfile import UserProfile 
from typing import Any
from .bases import MainUserDataSerializer
class UserProfileCreationSerializer(serializers.Serializer):
    bio:str = serializers.CharField(required = False)

    interest:list = serializers.ListField(
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
        data = super().to_representation(instance)
        user_data = MainUserDataSerializer(instance.user).data

        return {**data,**user_data}