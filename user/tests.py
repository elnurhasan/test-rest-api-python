from django.test import TestCase
from user.models import User
from blog.models import Post


class UserTestCase(TestCase):

    def setUp(self):
        self.first_user = User.objects.create(
            fullname='First user'
        )
        self.second_user = User.objects.create(
            fullname='Second user'
        )
        self.third_user = User.objects.create(
            fullname='Third user'
        )

    def test_subscribe_to_blog(self):
        blog = self.second_user.blog
        self.first_user.subscribe_to(blog)
        self.assertEqual(len(self.first_user.subscribed_blogs), 1)

        blog = self.third_user.blog
        self.first_user.subscribe_to(blog)
        self.assertEqual(len(self.first_user.subscribed_blogs), 2)

    def test_user_news_list(self):
        users = []
        for i in range(1000):
            users.append(
                User.objects.create(
                    fullname = f"User {i}"
                )
            )
        for user in users[:100]:
            Post.objects.create(
                blog = user.blog,
                title = f"Title {user.id}- {user.blog.id}",
                content = '',
            )
