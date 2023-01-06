from django.db import models
from django.conf import settings
import random,string

def get_random_id():
    id=random.choices(string.ascii_letters+string.digits,k=8)
    random.shuffle(id)
    return ''.join(id)


class Task(models.Model):
    id=models.CharField(primary_key=True,editable=False,max_length=8,default=get_random_id)
    title=models.CharField(max_length=255)
    description=models.TextField()
    assigned_user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    assigned_time=models.DateTimeField(auto_now=True)
    expired_time=models.DateTimeField()