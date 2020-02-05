from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=96)
    content = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)
    #thumbnail_file = models.ImageField(upload_to='images')
    thumbnail_url = models.URLField(null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    #comments_amount = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    publish_date = models.DateTimeField(default=datetime.now)
