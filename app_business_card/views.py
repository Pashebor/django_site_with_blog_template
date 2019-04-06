from django.shortcuts import render
from .models import MainPage, ContatcsPage, AboutUsPage


def render_page(request, page_name='main', page_model: object=MainPage):
    page_meta = page_model.objects.latest('id')
    context = {
        'meta': page_meta,
        'js': '/frontend/js/%s.bundle.js' % page_name,
        'css': '/frontend/css/%s.css' % page_name
    }
    return render(request, 'app_business_card/pages/%s/index.html' % page_name, context)


def main_page(request):
    return render_page(request)


def contacts(request):
    return render_page(request, 'contacts', ContatcsPage)


def about_us(request):
    return render_page(request, 'about_us', AboutUsPage)
