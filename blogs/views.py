from django.shortcuts import render,redirect
from .models import Blog,Category

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