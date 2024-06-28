from django.contrib import admin
from .models import Blog, Author, Editor

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Editor)
