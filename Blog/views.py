from django.utils import timezone
from django.shortcuts import render , get_object_or_404
from Blog.models import Post
def blog_page(request):
    posts = Post.objects.filter(status=1,publish_date__lte=timezone.now())
    context = {'posts':posts}
    return render(request,"blog/blog.html", context)
def single_page(request, pid):
    posts = Post.objects.filter(publish_date__lte=timezone.now(),status=1)
    post = get_object_or_404(posts , pk=pid)
    post.counted_views+=1
    post.save()
    context = {'post': post }
    return render(request,'blog/blog_single.html',context)
