from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.

def blog_homepage(request):
    blog_posts = Blog.objects
    return render(request, "blog/home.html", {'blog_posts':blog_posts})

def detailed_view(request, post_id):
    blog_post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/blog_post.html', {'blog_post':blog_post})
