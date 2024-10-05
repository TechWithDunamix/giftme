from rest_framework import serializers
from django.utils import timezone
from datetime import date
from ..models.userPosts import UserPost
from django.http import HttpRequest
class UserPostCreateSerializer(serializers.Serializer):

    title :str = serializers.CharField(required = True)

    body :str = serializers.CharField(required = True)

    images :list  = serializers.ListField(
        child = serializers.ImageField(),
        required = False
    )
    exlusive :bool = serializers.BooleanField(required = False,default = False)

    draft :bool = serializers.BooleanField(default = False,required = False)

    scheduled :bool = serializers.BooleanField(default = False)

    scheduled_for = serializers.DateTimeField(required = False)


    def validate_scheduled_for(self, value:date) -> date:
        
        if value < timezone.now():
            raise serializers.ValidationError("Can't schedule for a past date.")
        return value
    


class UserPostListSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    class Meta:
        model = UserPost
        fields = ["title","body","scheduled","scheduled_for","draft","exlusive","image"]


    def get_image(self,instance :UserPost):
        request :HttpRequest = self.context.get("request")
        if request:
            return request.build_absolute_uri(instance.images.first().image.url) if instance.images.first().image else None
        return " /// "
        
