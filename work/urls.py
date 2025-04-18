from django.urls import path
from work.views import * 

app_name = 'work'

urlpatterns = [
    path('',work_page,name='index'),
    path('single/<int:pid>',work_single,name='single'),

]