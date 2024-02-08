from django.db import models
from user.models import User


class Blog(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog', null=True, verbose_name='Author')

    def __str__(self) -> str:
        return self.author.fullname if self.author else 'Not set'


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post', null=True, verbose_name='Blog')
    title = models.CharField(max_length=128, verbose_name='Title')
    content = models.CharField(max_length=140, null=True, blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']

