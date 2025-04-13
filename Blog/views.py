from django.utils import timezone
from django.shortcuts import render
from Blog.models import Post
def blog_page(request):
    posts = Post.objects.filter(status=1,publish_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request,"blog/blog.html", context)
def single_page(request):
    return render(request,'blog/blog_single.html')