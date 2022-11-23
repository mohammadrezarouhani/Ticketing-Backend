from django.db import models
from django.contrib.auth.models import AbstractUser
import os,pathlib,uuid,random,string,pdb


def get_random_id():
    id=random.choices(string.ascii_letters+string.digits,k=8)
    random.shuffle(id)
    return ''.join(id)

def get_image_path(model,filename):
    folder_name= 'user_photo' if isinstance(model,BaseUser) else 'content_file'
    return os.path.join(folder_name,str(uuid.uuid4())+pathlib.Path(filename).suffix)


class BaseUser(AbstractUser):
    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    RANK=[
        ('MAN','MANAGER'),
        ('SUP','SUPERWISER'),
        ('STF','STAFF')
    ]
    MANAGER=('MAN','MANAGER')
    SUPERWISER=('SUP','SUPERWISER')
    STAFF=('STF','STAFF')

    departman=models.ForeignKey('Departman',on_delete=models.SET_NULL,null=True)
    email=models.EmailField(unique=True)
    rank=models.CharField(max_length=115,choices=RANK)
    has_message=models.PositiveIntegerField(default=0)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    image=models.ImageField(default='def.jpg',upload_to=get_image_path)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self) -> str:
        return self.email+"({})".format(self.id)

class Departman(models.Model):
    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    discription=models.TextField(null=True,blank=True)


class Ticket(models.Model):
    PRIORITY=[('H','HIGH'),('M','MIDIUM'),('L','LOW')]
    HIGH=('H','HIGH')
    MEDIUM=('M','MIDIUM')
    LOW=('L','LOW')

    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    discription=models.TextField()
    priority=models.CharField(max_length=115,choices=PRIORITY,default=MEDIUM)
    owner=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    departman=models.ForeignKey(Departman,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering=['-created_at']


class TicketMessage(models.Model):
    STATUS=[('SN','SEEN'),('US','UNSEEN')]
    SEEN=('SN','SEEN')
    UNSEEN=('US','UNSEEN')

    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE,related_name='ticket_message')
    sender=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='reciever')
    title=models.CharField(max_length=255)
    discription=models.TextField()
    status=models.CharField(max_length=115,choices=STATUS)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)


class TicketHistory(models.Model):
    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    owner=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    departman=models.ForeignKey(Departman,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']


class FileUpload(models.Model):
    ticket_message=models.ForeignKey(TicketMessage,on_delete=models.CASCADE,related_name='file_upload')
    image=models.FileField(upload_to=get_image_path)
    created_at=models.DateTimeField(auto_now=True)

