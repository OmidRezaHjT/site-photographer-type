from django import template
from Blog.models import Comment
register = template.Library()

@register.simple_tag(name='comments-count')
def function(pid):
    return Comment.objects.filter(post=pid, approach=True).order_by('-created_date').count()