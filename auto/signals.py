import pdb
from django.db.models.signals import pre_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model
import os
from . import models


@receiver(post_save,sender=models.Message )
def on_save_ticketmessage(sender,instance,created,*args,**kwargs):
    if created and instance.status == "US":
        user_profile=models.Profile.objects.get(user_id=instance.receiver.id)
        user_profile.has_message+=1
        user_profile.save()
        instance.save()


@receiver(pre_delete,sender=models.Message)
def on_delete_message(sender,instance,using,*args,**kwargs):
        user_profile=models.Profile.objects.get(id=instance.receiver.id)
        user_profile.has_message-=1
        user_profile.save()



@receiver(pre_delete,sender=models.MessageFile)
def on_delete_message_file(sender,instance,using,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.file.path)


@receiver(pre_delete,sender=models.Profile)
def on_delete_user(sender,instance,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)
