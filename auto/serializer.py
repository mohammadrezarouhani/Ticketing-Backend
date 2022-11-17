from rest_framework import serializers
from .import models

class BaseUserSerializer(serializers.ModelSerializer):
     
     class Meta:
        model=models.BaseUser
        fields='__all__'



class DepartmanSerializer(serializers.ModelSerializer):

    class Meta:
        fields='__all__'
        model=models.Departman


class TicketHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=models.TicketHistory


class FileUploadserializer(serializers.ModelSerializer):
    class Meta:
        fields=['id','ticket_message','image','created_at']
        model=models.FileUpload


class TicketMessageSerializer(serializers.ModelSerializer):
    file_upload=FileUploadserializer(many=True)

    class Meta:
        fields=['id','ticket','title','discription','created_at','file_upload']
        model=models.TicketMessage

    def create(self, validated_data):
        file_upload=validated_data.pop('file_upload')
        ticket_message=super().create(validated_data)

        for data in file_upload:
            models.FileUpload.objects.create(**data,ticket_message=ticket_message)

        return ticket_message

    def update(self, instance, validated_data):
        file_upload=validated_data.pop('file_upload')
        ticket_message=super().update(instance, validated_data)
        models.FileUpload.objects.filter(ticket_message=ticket_message).delete()
        
        for data in file_upload:
            models.FileUpload.objects.create(**data,ticket_message=ticket_message)
        return ticket_message

    
class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Ticket
        fields=['id','title','discription','priority','sender','reciever','departman','created_at','updated_at']

