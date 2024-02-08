from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
import lorem
from user.models import User, News
from blog.models import Blog, Post

class Command(BaseCommand):
    help = "Generate fake user name"

    def handle(self, *args, **options):
        print("Start fake Post generation")
        count = 0
        users = User.objects.all()
        for user in users:
            try:
                for i in range(2):
                    sentence = lorem.sentence()
                    paragraph = lorem.paragraph()
                    Post.objects.create(
                        blog = user.blog,
                        title = next(sentence)[:128],
                        content = next(paragraph)[:140]
                    )
                    count += 1
            except IntegrityError as err:
                print('IntegrityError:', err)
        print(f"Created {count} fake post")
        print("End fake Post generation")