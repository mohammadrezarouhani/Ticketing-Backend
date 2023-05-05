import pdb
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.db.models import Q,Count
from django.shortcuts import get_object_or_404
import os
from . import models


@receiver(post_save,sender=models.Profile)
def on_create_user_profile(sender,instance,created,*args,**kwargs):
    if created:
        message_count=models.Message.objects.filter(Q(sender_id=instance.user.id)\
                                                    |Q(receiver_id=instance.user.id)\
                                                    & Q(status='US'))\
                                                    .aggregate(message_count=Count('pk')) 
        instance.has_message=message_count['message_count']
        instance.save()                                               


@receiver(post_save,sender=models.Message)
def on_save_letter_message(sender,instance,created,*args,**kwargs):
    if created and instance.status == "US":
        user_profile=get_object_or_404(models.Profile,id=instance.receiver.id)
        user_profile.has_message+=1
        user_profile.save()
        instance.save()


@receiver(post_delete,sender=models.Message)
def on_delete_message(sender,instance,using,*args,**kwargs):
        user_profile=get_object_or_404(models.Profile,id=instance.receiver.id)
        user_profile.has_message-=1
        user_profile.save()



@receiver(post_delete,sender=models.Profile)
def on_delete_user(sender,instance,*args,**kwargs):
    if instance.photo and os.path.exists(instance.photo.path):
        os.remove(instance.photo.path)


@receiver(post_delete,sender=models.MessageFile)
def on_delete_message_file(sender,instance,using,*args,**kwargs):
    if os.path.exists(instance.image.path):
        os.remove(instance.file.path)


@receiver(post_delete,sender=models.ArchiveFile)
def on_delete_archive_file(sender,instance,using,*args,**kwargs):
    if os.path.exists(instance.file.path):
        os.remove(instance.file.path)