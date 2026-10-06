from django.shortcuts import render,redirect
from blogs.models import Category
from blogs.models import Blog
from assignments.models import About 
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import auth

def home(request):
  
    featured_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    # fetching about us 
    try:
        about = About.objects.get()
    except:
        about=None
    context ={
       
        'featured_posts' : featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html', context)

def register(request):
    error = None
    if request.method == 'POST':
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if password1 != password2:
              error="password doesn't match"
        else:
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
           else:
               error=form.errors

    return render(request, 'register.html', {'error':error})

def login(request):
    if request.method=='POST':
        form= AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=auth.authenticate(username=username ,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    form= AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('home')