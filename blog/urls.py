from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.blog_api, name='post-api'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
