from rest_framework import serializers 
from typing import List
from ..models.userMemberships import UserMembership
from django.http import HttpRequest
class UserMembershipCreateSerializer(serializers.Serializer):

    name:str = serializers.CharField()

    image  = serializers.ImageField(required = False)

    rewards :List[str] = serializers.ListField(
        child = serializers.CharField(),
        required = False
    )

    welcome_note :str = serializers.CharField()

    description :str = serializers.CharField()

    price_per_month :float = serializers.FloatField()

    price_per_year :float = serializers.FloatField()

    full_time :bool = serializers.BooleanField(required = False)

    max_members :int = serializers.IntegerField(default = 1000)

    limit_members :bool = serializers.BooleanField()


class UserMembershipsViewSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    class Meta:
        model = UserMembership

        fields :list = ["id","name","rewards","welcome_note",
                       "description","price_per_month",
                       "full_time", "max_members","limit_members",
                       "full_price","image"]



    def get_image(self, instance :UserMembership):
        request :HttpRequest = self.context.get("request")
        if instance.image:
            return request.build_absolute_uri(instance.image)
        
        return ""


class UserMembershipUpdateSerializer(serializers.Serializer):

    

    name:str = serializers.CharField(required = False)

    image  = serializers.ImageField(required = False)

    rewards :List[str] = serializers.ListField(
        child = serializers.CharField(),
        required = False
    )

    welcome_note :str = serializers.CharField(required = False)

    description :str = serializers.CharField(required = False)

    price_per_month :float = serializers.FloatField(required = False)

    price_per_year :float = serializers.FloatField(required = False)

    full_time :bool = serializers.BooleanField(required = False)

    max_members :int = serializers.IntegerField(default = 1000)

    limit_members :bool = serializers.BooleanField(required = False)
