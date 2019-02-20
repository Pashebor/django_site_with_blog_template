from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('contacts/', views.contacts, name='index'),
    path('about-us/', views.about_us, name='index'),
]
