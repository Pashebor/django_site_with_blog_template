from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from transliterate import translit


class BlogArticles(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')

    slug = models.SlugField(default='', blank=True, verbose_name='Url')

    preview_text = models.CharField(
        max_length=55,
        default='',
        verbose_name='Превью текст'
    )
    preview_image = models.ImageField(
        upload_to='uploads/preview/',
        blank=True,
        null=True,
        verbose_name='Превью изображение'
    )
    detail_image = models.ImageField(
        upload_to='uploads/details/',
        blank=True,
        null=True,
        verbose_name='Детальное изображение'
    )
    watches = models.CharField(
        max_length=1000,
        default=1,
        verbose_name='Кол-во просмотров'
    )
    desc = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Мета \"Description\"'
    )
    keywords = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Мета \"Keywords\"'
    )
    content = RichTextUploadingField(
        blank=True,
        null=True,
        verbose_name='Контент'
    )
    date_created = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата публикации')


    def save(self):
        if not self.slug:
            self.slug = slugify(translit(self.title, 'ru', reversed=True))
            super(BlogArticles, self).save()
        else:
            self.slug = self.slug
            super(BlogArticles, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Статьи"
