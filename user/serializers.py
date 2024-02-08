from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.http import Http404
from user.models import User, News
from blog.serializers import PostSerializer


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    post = PostSerializer(read_only=True)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(required=True, allow_blank=False, max_length=64)
    news_list = NewsSerializer(many=True, read_only=True)


    def create(self, validated_data):
        try:
            return User.objects.create(**validated_data)
        except:
            raise Http404()


    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.save()
        return instance
