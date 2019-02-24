from django.db import models
from meta.models import ModelMeta


class MainPage(models.Model, ModelMeta):
    title = models.CharField(max_length=200, verbose_name='Заголовок главной страницы')
    description = models.CharField(max_length=255, verbose_name='Description meta')
    keywords = models.CharField(max_length=255, verbose_name='Keywords meta')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Главная страница'


class ContatcsPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок страницы \"Контакты\"')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Страница \"Контакты\"'


class AboutUsPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок страницы \"О нас\"')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Страница \"О Нас\"'
