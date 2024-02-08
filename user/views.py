from .models import User, News
from .serializers import UserSerializer, NewsSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@api_view(['GET'])
def user_api(request, format=None):
    return Response({
        'Users': reverse('user-list', request=request, format=format),
        'News': reverse('news-list', request=request, format=format),
    })