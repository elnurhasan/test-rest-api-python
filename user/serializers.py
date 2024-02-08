from rest_framework import serializers
from user.models import User, News


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(required=True, allow_blank=False, max_length=64)
    news_list = serializers.PrimaryKeyRelatedField(many=True, queryset=News.objects.all())
    

    def create(self, validated_data):
        try:
            return User.objects.create(**validated_data)
        except Exception as err:
            pass

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.save()
        return instance
