
from django.urls import path
from Blog.views import * 

app_name = 'blog'

urlpatterns = [
    path('',blog_page,name='index'),
    path('single', single_page,name="single"),

]