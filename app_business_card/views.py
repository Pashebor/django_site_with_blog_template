from django.shortcuts import render


def main_page(request):
    return render(request, 'app_business_card/pages/main_page/index.html')


def contacts(request):
    return render(request, 'app_business_card/pages/contacts/index.html')


def about_us(request):
    return render(request, 'app_business_card/pages/about_us/index.html')
