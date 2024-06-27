from django.shortcuts import render
from .models import Blog

def home(request):
    context = {'message':'Hello there😉'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)