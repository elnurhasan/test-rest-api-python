from django.test import TestCase
from user.models import User, News
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


class NewsTestCase(TestCase):

    def setUp(self):
        self.users = []
        for i in range(1000):
            self.users.append(
                User.objects.create(
                    fullname = f"User {i}"
                )
            )
        for user in self.users[:100]:
            for s_user in self.users[100:110]:
                user.subscribe_to(s_user.blog)


    def test_user_news_list(self):
        posts = []
        for user in self.users[100:110]:
            posts.append(
                Post.objects.create(
                    blog = user.blog,
                    title = f"Title {user.id}- {user.blog.id}",
                    content = '',
                )
            )

        for user in self.users[:10]:
            self.assertTrue(bool(user.news_list.all()))
