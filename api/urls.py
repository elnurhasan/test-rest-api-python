from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_root, name='api'),
    path('users/', include('user.urls')),
    path('blog/', include('blog.urls')),
]
