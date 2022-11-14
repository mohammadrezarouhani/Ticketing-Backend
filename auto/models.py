from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUser(AbstractUser):
    departman=models.OneToOneField('Departman',on_delete=models.SET_NULL)
    image=models.ImageField(default='def.jpg',upload_to='user_photo')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']


class Departman(models.Model):
    title=models.CharField(max_length=255)
    discription=models.TextField(null=True,blank=True)


class Letter(models.Model):
    title=models.CharField(max_length=255)
    discription=models.TextField()
    reciever=models.ForeignKey(Departman,oo_delete=models.CASCADE)
    images=models.ImageField()


class Image(models.Model):
    pass