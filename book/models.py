from django.conf import settings
from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=64)