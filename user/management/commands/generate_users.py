from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from mixer.backend.django import mixer
from user.models import User, News
from blog.models import Blog, Post

class Command(BaseCommand):
    help = "Generate fake user name"

    def handle(self, *args, **options):
        print("Start fake User generation")
        count = 0
        for _ in range(1000000):
            try:
                User.objects.create(
                    fullname = mixer.faker.name()
                )
                count += 1
            except IntegrityError as err:
                print('IntegrityError:', err)
        print(f"Created {count} fake users")
        print("End fake User generation")