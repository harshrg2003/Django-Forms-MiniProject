from django.contrib import admin

# Register your models here.
from myapp.models import Post
admin.site.register(Post)