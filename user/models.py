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
