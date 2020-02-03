from django.db import models
from django.shortcuts import reverse
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)
    #comments_amount = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=datetime.now)
