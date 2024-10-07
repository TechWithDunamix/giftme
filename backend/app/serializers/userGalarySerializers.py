from rest_framework.serializers import Serializer
from rest_framework import serializers
class UserGalaryCreateSerializer(Serializer):

    title :str = serializers.CharField()

    
    exclusive :bool = serializers.BooleanField(default = False)

    description :str = serializers.CharField()

    
        

