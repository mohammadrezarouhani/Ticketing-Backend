from django.db.models.signals import pre_delete,post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from . import models
import os,pdb

@receiver(post_save,sender=models.TicketMessage )
def on_save_ticketmessage(sender,instance,created,*args,**kwargs):
    if created:
        instance.reciever.has_message+=1
        instance.save()


@receiver(pre_delete,sender=models.FileUpload)
def on_delete_message_file(sender,instance,using,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)


@receiver(pre_delete,sender=get_user_model())
def on_delete_user(sender,instance,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)
