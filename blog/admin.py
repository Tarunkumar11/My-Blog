from django.contrib import admin
from blog.models import Blog_post,Blog_comments,Query
# Register your models here.
admin.site.register(Blog_post)
admin.site.register(Blog_comments)
#admin.site.register(Signup)
admin.site.register(Query)
