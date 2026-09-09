from django.shortcuts import render
from blogs.models import Category
from blogs.models import Blog

def home(request):
  
    featured_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    context ={
       
        'featured_posts' : featured_posts,
        'posts':posts
    }
    return render(request,'home.html', context)