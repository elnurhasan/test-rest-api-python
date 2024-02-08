from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.http import Http404
from user.models import User, News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'user', 'post', 'is_read', 'created_at']


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
