from ..models.authModels import AuthUserModel 
from rest_framework import serializers

class MainUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserModel
        fields = ["first_name","last_name","email","username"]