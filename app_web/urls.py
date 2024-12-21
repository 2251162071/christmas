from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('gift/', views.gift_view, name='gift'),
    path('wishes/', views.wishes_view, name='wishes'),
    path('contact/', views.contact_view, name='contact'),

]

