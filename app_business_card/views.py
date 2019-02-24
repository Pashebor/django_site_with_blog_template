from django.shortcuts import render
from .models import MainPage

def main_page(request):
    page = MainPage.objects.latest('id')
    return render(request, 'app_business_card/pages/main_page/index.html')


def contacts(request):
    return render(request, 'app_business_card/pages/contacts/index.html')


def about_us(request):
    return render(request, 'app_business_card/pages/about_us/index.html')
