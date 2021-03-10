from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth
from users.models import User
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _







def blog_image_upload(instance, filename):
    return "blog_covers/{}".format(filename)

class Query(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)    
    Title = models.CharField(max_length=100)
    Content = models.TextField()

    def __str__(self):
        return self.Title


#this class only for a authenticated user which can post
class Blog_post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    text = RichTextField(blank=True,null=True,config_name='blog')
    create_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(null = True,blank = True)
    image = models.ImageField( blank=True, upload_to=blog_image_upload)


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

class FavoriteRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Blog_post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.username, self.room)
# class Blog_tags(models.Model):
class Blog_comments(models.Model):
    post = models.ForeignKey(Blog_post,related_name = 'comments',on_delete=models.SET_NULL, null=True)
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
        return reverse("home")



# class User(User,auth.models.PermissionsMixin):

#     def __str__(self):
#         return '@{}'.format(self.username)
