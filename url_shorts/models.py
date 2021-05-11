from django.db import models


# Create your models here.
class Urls(models.Model):
    """Store URLS and its Shortened version"""
    url = models.TextField(max_length=10000, unique=True, null=False)
    uuid = models.TextField(max_length=10, unique=True, null=False)


class Input(models.Model):
    url = models.TextField(max_length=10000, unique=True, null=False)

