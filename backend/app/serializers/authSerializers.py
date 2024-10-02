from rest_framework import serializers
from ..models.authModels import AuthUserModel
from rest_framework.exceptions import ValidationError
class UserSignupSerializer(serializers.Serializer):

    email:str = serializers.EmailField()

    password:str = serializers.CharField()

    first_name:str = serializers.CharField()

    last_name:str = serializers.CharField()

    country:str = serializers.CharField()

    username:str = serializers.CharField()

    def validate_email(self, value: str):
        if AuthUserModel.objects.filter(email = value).exists():
            raise serializers.ValidationError("User with this email already exists")
        return value

    def validate_username(self, value: str):
        if AuthUserModel.objects.filter(username = value).exists():
            raise serializers.ValidationError("User with this username already exists")
        return value


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()