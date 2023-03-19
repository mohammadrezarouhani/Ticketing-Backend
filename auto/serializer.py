from rest_framework import serializers
from .import models


class DepartmanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','title','description']
        model = models.Departman


class ProfileSerializer(serializers.ModelSerializer):
    has_message=serializers.ReadOnlyField()
    class Meta:
        model=models.Profile
        fields=['id','user_id','departman','rank','has_message','photo']


class SimpleLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Letter
        fields=['id','title']


class ArchiveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ArchiveFile
        fields=['id','archive_id','file']

    def create(self, validated_data):
        archive_pk=self.context.get('archive_pk')
        (archive,created)=models.Archive.objects.get_or_create(pk=archive_pk)
        validated_data['archive']=archive
        return super().create(validated_data)
    

class History(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Archive


class MessageFileserializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','message_id','file']
        model = models.MessageFile

    def create(self, validated_data):
        message_pk=self.context.get('message_pk')
        (message,created)=models.Message.objects.get_or_create(id=message_pk)
        validated_data['message']=message
        return super().create(validated_data)


class LetterSerializer(serializers.ModelSerializer):    
    class Meta:
        model = models.Letter
        fields = '__all__'

    def validate(self, attrs):
        sender=attrs['sender']
        reciever=attrs['receiver']
        if sender==reciever:
            raise serializers.ValidationError(detail='sender and reciever can not have a same value.')
        return super().validate(attrs)


class MessageSerializer(serializers.ModelSerializer):    
    class Meta:
        fields = '__all__'
        model = models.Message

    def validate(self, attrs):
        sender=attrs['sender']
        reciever=attrs['receiver']
        if sender==reciever:
            raise serializers.ValidationError('sender and reciever can not have a same value.')
        return super().validate(attrs)
