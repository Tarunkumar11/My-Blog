from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth

# Create your models here.

class Query(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)    
    Title = models.CharField(max_length=100)
    Content = models.TextField()

    def __str__(self):
        return self.Title


#this class only for a authenticated user which can post
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(null = True,blank = True)

    #for publish_date
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)
        #approve_comment = True this should be same to approve_comment = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",kwargs = {'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey('blog.POST',related_name = 'comments',on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length = 250)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()
    

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_list")



class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return '@{}'.format(self.username)
