from rest_framework.serializers import ModelSerializer
from . import models

class FileSerialzier(ModelSerializer):
    class Meta:
        fields=['id','type','file']
        model=models.File