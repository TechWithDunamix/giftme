from rest_framework.serializers import Serializer
from rest_framework import serializers
from ..models.userGalary import UserGalary
from django.http import HttpRequest
class UserGalaryCreateSerializer(Serializer):
    images  = serializers.ListField(
        child = serializers.ImageField()
    )

    title :str = serializers.CharField()

    
    exclusive :bool = serializers.BooleanField(default = False)

    description :str = serializers.CharField()

    
        


class UserGalaryListSerializer(serializers.ModelSerializer):
    images  = serializers.SerializerMethodField()
    class Meta:
        model = UserGalary
        fields = ["id",'title', 'exclusive','description', 'images']


    def get_images(self, instance :UserGalary):
        request :HttpRequest = self.context.get("request",None)
        if request:
            return [request.build_absolute_uri(img.image.url) for img in instance.get_image_list()]
        return ''


class UserGalaryUpdateSerializer(Serializer):

    title :str = serializers.CharField()

    
    exclusive :bool = serializers.BooleanField(default = False)

    description :str = serializers.CharField()