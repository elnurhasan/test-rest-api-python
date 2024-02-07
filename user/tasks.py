from celery import shared_task
from django.conf import settings as conf_settings
from .models import User

@shared_task()
def sheduler_task():
    print('Send email last subscribed blog post')


@shared_task()
def delete_addition_news(user_id):
    print(user_id)
    try:
        user = User.objects.get(pk=int(user_id))
        for_delete_news = user.news_list.all()[conf_settings.POST_SIZE_IN_NEWS_LIST_FOR_USER:]
        for news in for_delete_news:
            news.delete()
    except Exception as err:
        print('Exception in delete_addition_news:', err)
