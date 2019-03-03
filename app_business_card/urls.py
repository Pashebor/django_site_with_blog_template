from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('contacts/', views.contacts, name='index'),
    path('about-us/', views.about_us, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
