from django.db import models

class Subscribe(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='subscribes')
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='subscribes')
