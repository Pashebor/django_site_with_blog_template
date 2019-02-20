from django.shortcuts import render
from .models import BlogArticles


def get_all_articles():
    all_articles = BlogArticles.objects.all()

    context = {
        'name': 'Блог',
        'title': 'Блог',
        'posts': all_articles
    }
    return context


def blog_preview(request):
    return render(request, 'blog/index.html', get_all_articles())


def blog_article(request):
    return render(request, 'blog/index.html')
