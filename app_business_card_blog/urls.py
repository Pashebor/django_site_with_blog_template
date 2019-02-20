from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_preview, name='index'),
    path('^(?P<id>\d+)/$', views.blog_article, name='detail'),
]