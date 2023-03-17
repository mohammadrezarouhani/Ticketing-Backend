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


class FileHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.FileHistory
        fields='__all__'


class History(serializers.ModelSerializer):
    history_file=FileHistorySerializer(many=True,allow_null=True)

    class Meta:
        fields = '__all__'
        model = models.History

    def create(self, validated_data):
        history_file=validated_data.pop('history_file')
        history=super().create(validated_data)

        for data in history_file:
            models.FileHistory.objects.create(**data,history=history)
        
        return history

    def update(self, instance, validated_data):
        history_file=validated_data.pop('history_file')
        history=super().update(instance, validated_data)
        models.FileHistory.objects.filter(history=history).delete()

        for data in history_file:
            models.FileHistory.objects.create(**data,history=history)

        return history


class CommentFileserializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.CommentFile


class LetterSerializer(serializers.ModelSerializer):
    departman_detail=DepartmanSerializer(source='departman',read_only=True)
    
    class Meta:
        model = models.Letter
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    comment_file=CommentFileserializer(many=True)
    
    class Meta:
        fields = '__all__'
        model = models.Comment

    def create(self, validated_data):
        comment_file = validated_data.pop('comment_file')
        comment = super().create(validated_data)

        for data in comment_file:
            models.CommentFile.objects.create(**data, comment=comment)
        return comment

    def update(self, instance, validated_data):
        comment_file = validated_data.pop('comment_file')
        comment = super().update(instance, validated_data)
        models.CommentFile.objects.filter(comment=comment).delete()

        for data in comment_file:
            models.CommentFile.objects.create(**data, comment=comment)
        return comment


class CommentStatusSerializer(serializers.Serializer):
    comment_id=serializers.CharField()
    date=serializers.DateTimeField()

