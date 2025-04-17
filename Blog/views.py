from django.utils import timezone
from django.shortcuts import render , get_object_or_404
from Blog.models import Post , Comment
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from Blog.forms import CommentForm
from django.contrib import messages

def blog_page(request,cat_name=None,author_username=None,tag_name=None):
    posts = Post.objects.filter(status=1,publish_date__lte=timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if tag_name:
        posts = posts.filter(tag__name__in=[tag_name])
    posts= Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)    
    context = {'posts':posts}
    return render(request,"blog/blog.html", context)
def single_page(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ur comment successfully sent")
        else:
             print(form.errors)
             messages.add_message(request, messages.ERROR, "Ur comment didnt sent")
    posts = Post.objects.filter(publish_date__lte=timezone.now(),status=1)
    comments = Comment.objects.filter(post=pid,approach=True)
    form = CommentForm()
    post = get_object_or_404(posts , pk=pid)
    comments = Comment.objects.filter(post=pid, approach=True).order_by('-created_date')
    post.counted_views+=1
    post.save()
    context = {'post': post , 'comments' : comments , 'form' : form }
    return render(request,'blog/blog_single.html',context)
