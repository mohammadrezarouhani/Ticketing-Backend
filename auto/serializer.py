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


class FileHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.FileHistory
        fields='__all__'


# oeverridong create and update method 
class History(serializers.ModelSerializer):
    history_file=FileHistorySerializer(many=True,allow_null=True)
    class Meta:
        fields = '__all__'
        model = models.History


class CommentFileserializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'comment', 'image', 'created_at']
        model = models.CommentFile


class LetterCommentSerializer(serializers.ModelSerializer):
    comment_file = CommentFileserializer(many=True,allow_null=True)

    class Meta:
        fields = ['id', 'letter', 'sender', 'receiver', 'title',
                  'description', 'status','created_at','updated_at', 'comment_file']
        model = models.Comment

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


class InitialLetterSerializer(serializers.ModelSerializer):
    comment=CommentFileserializer(many=True)
    
    class Meta:
        fields=['id','priority','owner','departman','comment']
        model=models.Letter

class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(max_length=115)
    new_password=serializers.CharField(max_length=115)


class CommentStatusSerializer(serializers.Serializer):
    comment_id=serializers.CharField()
    date=serializers.DateTimeField()