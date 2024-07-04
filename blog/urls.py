from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),
    path("editors/",views.editor_list, name="editor_list"),
    path('add_blog', views.add_blog, name='add_blog')
]
