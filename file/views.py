from django.shortcuts import render
from django.conf import settings
from rest_framework import views,status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser,FormParser
from pathlib import Path
import datetime
# Create your views here.

class FileUploadAPiView(views.APIView):
    parser_classes=[MultiPartParser,FormParser]

    def post(self,request,format=None):
        file=request.FILES['file']
        type=request.query_params.get('type')

        year_month=datetime.datetime.now().strftime(r'%h-%Y')
        day=datetime.datetime.now().strftime(r'%d')
        time=datetime.datetime.now().strftime(r'%H-%M-%S-%f')
        file_path=Path(settings.MEDIA_ROOT)

        # choosing what folder file should be saved to 
        if type=='user':    
            folder='user'
        elif type=='history':
            folder='history_file'
        else :
            folder='content_file'
        
        file_name=time+Path(file._name).suffix
        file_path=file_path.joinpath(folder).joinpath(year_month).joinpath(day)

        file_path.mkdir(parents=True,exist_ok=True)
        file_path=file_path.joinpath(file_name)

        # file url for browsing 
        file_url=settings.MEDIA_URL+'/'+folder+'/'+year_month+'/'+day+'/'+file_name

        if file:
            with open (file_path,mode='wb+') as temp_file:
                for chunk in file.chunks():
                    temp_file.write(chunk)
            
            return Response(data={'file':file_url})
        
        return Response(status=status.HTTP_400_BAD_REQUEST)