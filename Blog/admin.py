from django.contrib import admin
from Blog.models import Post , Category
from django_summernote.admin import SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author' ,'counted_views','login_require','status','publish_date','created_date')
    list_filter = ('status','author')
    search_fields = ['title','content']
    summernote_fields = ('content',)


admin.site.register(Category)
admin.site.register(Post,PostAdmin)  