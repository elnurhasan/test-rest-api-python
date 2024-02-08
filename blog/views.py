from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def blog_api(request, format=None):
    return Response({
        'Post': reverse('post-list', request=request, format=format),
    })