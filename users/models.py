from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class BaseUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone=models.CharField(max_length=15,validators=[phone_regex],default="+914000000")

    
    def __str__(self) -> str:
        return self.username+"({})".format(self.id)