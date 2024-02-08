from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscribe
from user.tasks import build_news_list


@receiver(post_save, sender=Subscribe)
def signal_create_subscribe(sender, instance, created, **kwargs):
    if created:
        build_news_list.delay(instance.id)
