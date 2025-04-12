from django.urls import path
from website.views import *
urlpatterns = [
    path('',home_page,name='index'),
    path('contact',contact_page,name='contact'),
    path('about',about_page,name='about'),
    
]
