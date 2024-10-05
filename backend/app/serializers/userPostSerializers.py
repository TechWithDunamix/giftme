from rest_framework import serializers
from django.utils import timezone
from datetime import date
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
    

