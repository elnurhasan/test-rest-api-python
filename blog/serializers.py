from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.http import Http404
from .models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=128)
    content = serializers.CharField(required=True, allow_blank=False, max_length=140)
    created_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
