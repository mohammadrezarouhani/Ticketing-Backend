from django.db.models.signals import pre_delete,post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import BaseUser
from . import models
import os,pdb

@receiver(post_save,sender=models.Comment )
def on_save_ticketmessage(sender,instance,created,*args,**kwargs):
    if created and instance.status == "US":
        user=get_user_model().objects.get(id=instance.receiver.id)
        user.has_message+=1
        user.save()
        instance.save()


@receiver(pre_delete,sender=models.Comment)
def on_delete_message(sender,instance,using,*args,**kwargs):
        user=get_user_model().objects.get(id=instance.receiver.id)
        user.has_message-=1
        user.save()


@receiver(pre_delete,sender=models.CommentFile)
def on_delete_message_file(sender,instance,using,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)


@receiver(pre_delete,sender=get_user_model())
def on_delete_user(sender,instance,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)
