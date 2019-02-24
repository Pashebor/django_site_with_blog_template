from django.shortcuts import render
from .models import BlogArticles


def get_all_articles():
    all_articles = BlogArticles.objects.all()

    context = {
        'name': 'Блог',
        'title': 'Блог',
        'meta': {
            'description': 'Hello',
            'keywords': 'key, word',
            'title': 'Test Blog'
        },
        'articles': all_articles
    }
    return context


def blog_preview(request):
    return render(request, 'blog/index.html', get_all_articles())


def blog_article(request, slug):
    article = BlogArticles.objects.get(slug=slug)
    context = {
        'meta': {
            'description': article.desc,
            'keywords': article.keywords,
            'title': article.title
        },
        'article': article
    }
    return render(request, 'blog/article.html', context)
