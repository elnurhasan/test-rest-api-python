from django.test import TestCase
from user.models import User
from blog.models import Blog


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
