from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
import os,pathlib,uuid,random,string,pdb,datetime


def get_random_id():
    id=random.choices(string.ascii_letters+string.digits,k=8)
    random.shuffle(id)
    return ''.join(id)

def get_image_path(model,filename):

    date_moth=datetime.datetime.now().strftime('%h-%Y')
    date_day=datetime.datetime.now().strftime(r"%d-%H-%M-%S")

    folder_name= 'user_file' if isinstance(model,BaseUser) else 'content_file'
    folder_name=os.path.join(folder_name,date_moth)
    return os.path.join(folder_name,date_day+pathlib.Path(filename).suffix)


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
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone=models.CharField(max_length=15,validators=[phone_regex],default="+914000000")
    departman=models.ForeignKey('Departman',on_delete=models.SET_NULL,null=True,related_name='departman_detail')
    email=models.EmailField(unique=True)
    rank=models.CharField(max_length=115,choices=RANK,default=STAFF)
    has_message=models.PositiveIntegerField(default=0)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    image=models.ImageField(default='def.jpg',upload_to=get_image_path)
    
    def __str__(self) -> str:
        return self.username+"({})".format(self.id)


class Departman(models.Model):
    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title+"({})".format(id)


class Letter(models.Model):
    PRIORITY=(('H','HIGH'),('M','MIDIUM'),('L','LOW'))
    HIGH=('H','HIGH')
    MEDIUM=('M','MIDIUM')
    LOW=('L','LOW')

    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=255)
    priority=models.CharField(max_length=115,choices=PRIORITY,default=MEDIUM)
    owner=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    departman=models.ForeignKey(Departman,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return "letter"+str(self.title)+" ({})".format(self.id)

    class Meta:
        ordering=['-created_at']


class Comment(models.Model):
    STATUS=[('SN','SEEN'),('US','UNSEEN')]
    SEEN=('SN','SEEN')
    UNSEEN=('US','UNSEEN')

    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    letter=models.ForeignKey(Letter,on_delete=models.CASCADE,related_name='comment',null=True)
    sender=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='reciever')
    title=models.CharField(max_length=255)
    description=models.TextField()
    status=models.CharField(max_length=115,choices=STATUS)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title+"({})".format(self.id)

    class Meta:
        ordering=['-created_at']
 

class CommentFile(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='comment_file',blank=True)
    file=models.FileField(default="def.jpg",upload_to=get_image_path)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self) -> str:
        return self.file.url+"({})".format(self.id)    

        
class History(models.Model):
    id=models.CharField(max_length=15,default=get_random_id,primary_key=True,unique=True,editable=False)
    title=models.CharField(max_length=115)
    description=models.TextField()
    owner=models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    departman=models.ForeignKey(Departman,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-created_at']

    def __str__(self) -> str:
        return self.title+"({})".format(self.id)
    

class FileHistory(models.Model):
    id=models.CharField(max_length=15,default=get_random_id
                        ,primary_key=True,unique=True,editable=False)
    history=models.ForeignKey(History,on_delete=models.CASCADE,related_name='history_file',blank=True)
    file=models.FileField(upload_to=get_image_path)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
        
    def __str__(self) -> str:
        return self.file.url+"({})".format(self.id)