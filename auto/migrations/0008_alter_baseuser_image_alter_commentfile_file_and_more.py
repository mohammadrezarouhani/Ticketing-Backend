# Generated by Django 4.1.5 on 2023-01-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0007_alter_comment_options_alter_commentfile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='image',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='commentfile',
            name='file',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='filehistory',
            name='file',
            field=models.CharField(max_length=512),
        ),
    ]
