from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.user_api, name='user-api'),
    path('list/', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('news/', views.NewsList.as_view(), name='news-list'),
    path('<int:user_id>/news/', views.news_list, name='news-list-by_id'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
