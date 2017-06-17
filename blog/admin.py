# Register your models here.

from django.contrib import admin


from .models import Post
# from the current directory ka models.py file we want to import Post


# To make our site visible on the admin page
admin.site.register(Post)