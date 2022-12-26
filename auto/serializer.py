from rest_framework import serializers
from .import models


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BaseUser
        fields = ['id','has_message','first_name','last_name','username','email','password','departman','rank']

    def create(self, validated_data):
        user=models.BaseUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class DepartmanSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Departman


class TicketHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.History


class FileUploadserializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'ticket_message', 'image', 'created_at']
        model = models.CommentFile


class LetterCommentSerializer(serializers.ModelSerializer):
    comment_file = FileUploadserializer(many=True,allow_null=True)

    class Meta:
        fields = ['id', 'letter', 'sender', 'receiver', 'title',
                  'description', 'status','created_at','updated_at', 'comment_file']
        model = models.LetterMessage

    def create(self, validated_data):
        file_upload = validated_data.pop('file_upload')
        letter_message = super().create(validated_data)

        for data in file_upload:
            models.CommentFile.objects.create(
                **data, letter_message=letter_message)
        return letter_message

    def update(self, instance, validated_data):
        file_upload = validated_data.pop('file_upload')
        letter_message = super().update(instance, validated_data)
        models.CommentFile.objects.filter(
            letter_message=letter_message).delete()

        for data in file_upload:
            models.CommentFile.objects.create(
                **data, letter_message=letter_message)
        return letter_message


class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Letter
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(max_length=115)
    new_password=serializers.CharField(max_length=115)


class CommentStatusSerializer(serializers.Serializer):
    comment_id=serializers.CharField()
    date=serializers.DateTimeField()