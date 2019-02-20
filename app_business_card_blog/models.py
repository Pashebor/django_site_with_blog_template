from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class BlogArticles(models.Model):
    title = models.CharField(max_length=200)
    watches = models.CharField(max_length=1000, default=1)
    desc = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200, default=200)
    content = RichTextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Статьи"
