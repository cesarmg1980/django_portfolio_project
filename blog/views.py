from django.shortcuts import render
from blog.models import Blog

# Create your views here.

def blog_homepage(request):
    blog_posts = Blog.objects
    return render(request, "blog/home.html", {'blog_posts':blog_posts})
