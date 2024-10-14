from rest_framework import serializers
from ..models import UserPost 
from django.http import HttpRequest
class SponsorsPostFeedListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserPost

        fields = ["title","date_created","id","exlusive", "image", "user"]


    def get_image(self,instance :UserPost):
        request :HttpRequest = self.context.get("request")
        image = instance.get_image_list()[0]
        return request.build_absolute_uri(image.image) if image.image else ""

    def get_user(self, instance :UserPost):
        request :HttpRequest = self.context.get("request")

        user_data = {
            "username" : instance.user.username,
            "id" :  instance.user.id,
            "profile_image" : request.build_absolute_uri(instance.user.user_profile.profile_image) if instance.user.user_profile.profile_image else ""
        }

        return user_data


