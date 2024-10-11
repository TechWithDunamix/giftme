from rest_framework import serializers 

class SponsorCreateSerializer(serializers.Serializer):

    email :str = serializers.EmailField()