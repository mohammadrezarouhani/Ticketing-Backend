from django.db import models
from django.conf import settings
from . import path_generator as pathes


class Profile(models.Model):
    RANK=[
        ('chf','chief'),
        ('man','manager'),
        ('emp','employee')
    ]
    CHIEF=('chf','chief')
    MANAGER=('man','manager')
    EMPLOYEE=('emp','employee')

    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    departman=models.ForeignKey('Departman',on_delete=models.SET_NULL,null=True)
    rank=models.CharField(max_length=25,choices=RANK)
    has_message=models.PositiveIntegerField(default=0)
    photo=models.FileField(upload_to=pathes.profile_image_upload,blank=True,null=True)


class Departman(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title+"({})".format(self.id)


class Letter(models.Model):
    PRIORITY=(('H','HIGH'),('M','MIDIUM'),('L','LOW'))
    HIGH=('H','HIGH')
    MEDIUM=('M','MIDIUM')
    LOW=('L','LOW')
    STATUS=(('c','close'),('o','open'))
    CLOSE=('c','c')
    OPEN=('o','o')

    title=models.CharField(max_length=255)
    priority=models.CharField(max_length=115,choices=PRIORITY,default=MEDIUM)
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='letter_sender')
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='letter_receiver')
    departman=models.ForeignKey(Departman,on_delete=models.SET_NULL,null=True)
    status=models.CharField(choices=STATUS,default=OPEN,max_length=25)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return "letter"+str(self.title)+" ({})".format(self.id)

    class Meta:
        ordering=['-created_at']


class Message(models.Model):
    STATUS=[('SN','SEEN'),('US','UNSEEN')]
    SEEN=('SN','SEEN')
    UNSEEN=('US','UNSEEN')

    letter=models.ForeignKey(Letter,on_delete=models.CASCADE,related_name='comment',null=True)
    sender=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reciever')
    title=models.CharField(max_length=255)
    description=models.TextField()
    status=models.CharField(max_length=115,choices=STATUS)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title+"({})".format(self.id)

    class Meta:
        ordering=['-created_at']


class MessageFile(models.Model):
    message=models.ForeignKey(Message,on_delete=models.CASCADE,related_name='comment_file',blank=True)
    file=models.FileField(upload_to=pathes.message_file_upload)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self) -> str:
        return self.file+"({})".format(self.id)    


class Archive(models.Model):
    title=models.CharField(max_length=115)
    description=models.TextField()
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    departman=models.ForeignKey(Departman,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-created_at']

    def __str__(self) -> str:
        return self.title+"({})".format(self.id)


class ArchiveFile(models.Model):
    archive=models.ForeignKey(Archive,on_delete=models.CASCADE,related_name='history_file',blank=True)
    file=models.FileField(upload_to=pathes.archive_file_upload)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
        
    def __str__(self) -> str:
        return self.file.path+"({})".format(self.id)