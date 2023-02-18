from django.db import models
import datetime,pathlib,os


def get_file_path(model,filename):#TODO creating new path for uploading file 
    date_moth=datetime.datetime.now().strftime('%h-%Y')
    date_day=datetime.datetime.now().strftime(r"%d-%H-%M-%S")
    
    folder_name=os.path.join(folder_name,date_moth)
    return os.path.join(folder_name,date_day+pathlib.Path(filename).suffix)


class File(models.Model):
    type=models.CharField(max_length=25)
    file=models.FileField(upload_to=get_file_path)