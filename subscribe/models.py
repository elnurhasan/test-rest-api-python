from django.db import models
from user.models import User
from blog.models import Blog

class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribes')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='subscribes')
