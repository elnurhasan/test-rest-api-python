from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
import lorem
from user.models import User, News
from blog.models import Blog, Post

class Command(BaseCommand):
    help = "Simulate subscribe"

    def handle(self, *args, **options):
        users = User.objects.all()[:1000]
        for user in users[:100]:
           for s_user in users[100:200]:
               user.subscribe_to(s_user.blog)