from rest_framework import serializers

class ReactionSerializer(serializers.Serializer):

    reaction :str = serializers.CharField()
