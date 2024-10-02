from rest_framework import serializers
from ..models.authModels import AuthUserModel
class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUserModel 

        fields = ["email","first_name","last_name","username","password"]
        


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()