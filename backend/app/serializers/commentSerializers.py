from rest_framework import serializers

class CommentSerializer(serializers.Serializer):

    text :str = serializers.CharField()
