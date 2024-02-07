from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from blog.models import Post
from subscribe.models import Subscribe
from user.tasks import delete_addition_news


@receiver(post_save, sender=Post)
def signal_create_fill_news_list(sender, instance, created, **kwargs):
    if created:
        subscribes = Subscribe.objects.filter(blog=instance.blog).all()
        for subscribe in subscribes:
            subscribe.user.add_post_to_news_list(instance)
            delete_addition_news.delay(subscribe.user.id)

