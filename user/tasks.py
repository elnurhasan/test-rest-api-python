from celery import shared_task
from django.conf import settings as conf_settings
from .models import User, News
from subscribe.models import Subscribe
from blog.models import Post

@shared_task()
def sheduler_task():
    print('Send email last subscribed blog post')


@shared_task()
def delete_addition_news(user_id):
    print(user_id)
    try:
        user = User.objects.get(pk=user_id)
        for_delete_news = user.news_list.all()[conf_settings.POST_SIZE_IN_NEWS_LIST_FOR_USER:]
        for news in for_delete_news:
            news.delete()
    except Exception as err:
        print('Exception in delete_addition_news:', err)


@shared_task()
def build_news_list(subscribe_id):
    try:
        subscribe = Subscribe.objects.get(pk=subscribe_id)
        user = User.objects.get(pk=subscribe.user.id)
        user_news = list(user.news_list.all())
        user_posts = list(subscribe.blog.post.all())
        data_list = user_news + user_posts
        sorted_list = sorted(data_list, key=lambda x: x.created_at, reverse=True)
        for item in sorted_list:
            if type(item) == Post:
                News.objects.create(
                    user = subscribe.user,
                    post = item,
                    is_read = False,
                    created_at = item.created_at
                )

    except Exception as err:
        print('Exception in delete_addition_news:', err)
