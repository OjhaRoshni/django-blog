from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Category

from django.db.models import Q

# Create your views here.

def post_by_category(request,category_id):
    # fetch yhe posts that belong to the category with the category_id
    posts = Blog.objects.filter(status='Published', category=category_id)

#   try/except we use if we want to do some custom action if the category doesn't exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # we can use get_object_or_404 when we want to show 404 error page
    # category = get_object_or_404(Category,pk=category_id)

    context ={
        'posts':posts,
        'category':category,
    }
    return render(request, 'posts_by_category.html',context)


def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context ={
        'single_blog':single_blog,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword)| Q(short_description__icontains=keyword)| Q(blog_body__icontains=keyword),status='Published')
    # print(blogs)
    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)