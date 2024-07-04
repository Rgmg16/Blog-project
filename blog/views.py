from django.shortcuts import render
from .models import Blog,Editor
from .forms import BlogForm
from django.shortcuts import redirect

def home(request):
    context = {'message':'Hello there😉'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

def editor_list(request):
    editors = Editor.objects.all()
    return render(request, 'editor_list.html', {'editors': editors})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()  
            return redirect('blog_list')  
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})