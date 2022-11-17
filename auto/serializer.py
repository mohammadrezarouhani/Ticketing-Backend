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


class FileUploadserializer(serializers.ModelSerializer):
    class Meta:
        fields=['id','letter','image','created_at']
        models=models.FileUpload


class TicketMessageSerializer(serializers.ModelSerializer):
    file_upload=FileUploadserializer(many=True)

    class Meta:
        fields=['id','letter','title','discription','created_at','file_upload']
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
    ticket_message=models.TicketMessage(many=True)

    class Meta:
        model=models.Ticket
        fields=['id','title','discription','priority','sender','receiver','departman','created_at','updated_at','ticket_message']

    def create(self, validated_data):
        ticket_message=validated_data.pop('ticket_message')
        ticket=models.Ticket.objects.create(**validated_data)
        for data in ticket_message:
            models.TicketMessage.objects.create(**data,ticket=ticket)

        return ticket

    def update(self, instance, validated_data):
        ticket_message=validated_data.pop('ticket_message')
        ticket=super().update(instance, validated_data)
        models.TicketMessage.objects.filter(ticket=ticket).delete()

        for data in ticket_message:
            models.TicketMessage.objects.create(**data,ticket=ticket)
            
        return ticket
