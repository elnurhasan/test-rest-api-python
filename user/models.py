from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=64, verbose_name='Full name', unique=True)

    def __str__(self) -> str:
        return self.fullname