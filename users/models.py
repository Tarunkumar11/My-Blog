from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib import auth


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, is_superuser=False, is_staff=False, **kwargs):
        user = self.model(email=email, is_superuser=is_superuser, is_staff=is_staff, **kwargs)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, is_superuser=False, is_staff=False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, is_superuser=True, is_staff=True, **kwargs)

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(blank=True, max_length=20)
    linkedin = models.TextField( max_length=150, null=True, blank=True)
    twitter = models.TextField( max_length=150, null=True, blank=True)
    Instagram = models.TextField( max_length=150, null=True, blank=True)

    def __str__(self):
        return '@{}'.format(self.username)
    class Meta:
        permissions = (("attachments.add_attachments", "Can add attachment"),
                       ("attachments.delete_attachments","Can delete attachment"),
                       ("attachments.delete_foreign_attachments","Can delete foreign attachments"))
        ordering = ['email']
    objects = UserManager()

class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    def __str__(self):
        return 'image_id: {} for user: {}'.format(self.pk, self.user)