
from django.urls import path
from Blog.views import * 

app_name = 'blog'

urlpatterns = [
    path('',blog_page,name='index'),
    path('<int:pid>', single_page,name="single"),
    path('category/<str:cat_name>',blog_page,name='category'),
    path('tag/<str:tag_name>',blog_page,name='tag'),
    path('author/<str:author_username>',blog_page,name='author'),

]