from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.http import Http404
from user.models import User, News


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(required=True, allow_blank=False, max_length=64)


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.save()
        return instance


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'user', 'post', 'is_read', 'created_at']
