from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.blog_preview, name='index'),
    url('^(?P<slug>[\w-]+)/$', views.blog_article, name='detail'),
]