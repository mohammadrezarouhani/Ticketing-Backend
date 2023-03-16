from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class BaseUser(AbstractUser):
    # RANK=[
    #     ('MAN','MANAGER'),
    #     ('SUP','SUPERWISER'),
    #     ('STF','STAFF')
    # ]

    # MANAGER=('MAN','MANAGER')
    # SUPERWISER=('SUP','SUPERWISER')
    # STAFF=('STF','STAFF')
    
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone=models.CharField(max_length=15,validators=[phone_regex],default="+914000000")
    # departman=models.ForeignKey('Departman',on_delete=models.SET_NULL,null=True,related_name='departman_detail')
    # email=models.EmailField(unique=True)
    # rank=models.CharField(max_length=115,choices=RANK,default=STAFF)
    # has_message=models.PositiveIntegerField(default=0)
    # is_staff=models.BooleanField(default=False)
    # is_superuser=models.BooleanField(default=False)
    # image=models.CharField(max_length=512)
    
    def __str__(self) -> str:
        return self.username+"({})".format(self.id)