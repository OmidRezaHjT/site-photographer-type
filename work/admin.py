from django.contrib import admin
from work.models import *

class WorkAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','created_date' , 'status' )
    list_filter = ('title','created_date', 'status')

admin.site.register(Album)
admin.site.register(Work,WorkAdmin)