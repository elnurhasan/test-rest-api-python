from django.test import TestCase
from user.models import User
from blog.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_blog_when_user_created(self):
        before_blogs = Blog.objects.count()
        user = User.objects.create(
            fullname='Test user'
        )
        after_blogs = Blog.objects.count()
        self.assertNotEqual(before_blogs, after_blogs)

    def test_delete_blog_when_user_deleted(self):
        before_blogs = Blog.objects.count()
        user = User.objects.create(
            fullname='Test user'
        )
        user.delete()
        after_blogs = Blog.objects.count()

        self.assertEqual(before_blogs, after_blogs)