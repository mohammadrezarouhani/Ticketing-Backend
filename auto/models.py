from django.db import models
from django.contrib.auth.models import AbstractUser
import os,pathlib,uuid,random,string


class BaseUser(AbstractUser):
    email=models.EmailField(unique=True)
    # image=models.ImageField(default='def.jpg',upload_to='user_photo')
    is_staff=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']


class Departman(models.Model):
    title=models.CharField(max_length=255)
    discription=models.TextField(null=True,blank=True)
    user=models.ForeignKey(BaseUser,on_delete=models.CASCADE)


class Ticket(models.Model):
    PRIORITY=[('H','HIGH'),('M','MIDIUM'),('L','LOW')]
    HIGH=('H','HIGH')
    MEDIUM=('M','MIDIUM')
    LOW=('L','LOW')

    title=models.CharField(max_length=255)
    discription=models.TextField()
    priority=models.CharField(max_length=115,choices=PRIORITY,default=MEDIUM)
    sender=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='sender')
    reciever=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='reciever')
    departman=models.ForeignKey(Departman,on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)


class TicketMessage(models.Model):
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='ticket_message')
    title=models.CharField(max_length=255)
    discription=models.TextField()
    create_at=models.DateTimeField(auto_now=True)


class TicketHistory(models.Model):
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    owner=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    departman=models.ForeignKey(Departman,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)



def get_image_path(model,filename):
    return os.path.join('content_file',str(uuid.uuid4())+pathlib.Path(filename).suffix)

class FileUpload(models.Model):
    ticket_message=models.ForeignKey(TicketMessage,on_delete=models.CASCADE,related_name='file_upload')
    image=models.FileField(upload_to=get_image_path)
    created_at=models.DateTimeField(auto_now=True)

