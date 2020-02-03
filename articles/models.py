from django.db import models
from django.shortcuts import reverse
from datetime import datetime

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
