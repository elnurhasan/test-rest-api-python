from django.db import models
from subscribe.models import Subscribe

class User(models.Model):
    fullname = models.CharField(max_length=64, verbose_name='Full name', unique=True)

    def __str__(self) -> str:
        return self.fullname
    
    def subscribe_to(self, blog) -> bool:
        """Subscribes the user to other users' blogs"""
        Subscribe.objects.create(
            user = self,
            blog = blog
        )

    @property
    def subscribed_blogs(self):
        return self.subscribes.all()
    
    def add_post_to_news_list(self, post):
        News.objects.create(
            user = self,
            post = post,
            is_read = False
        )


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_list')
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='in_news_list')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    def __str__(self) -> str:
        return self.post.title
