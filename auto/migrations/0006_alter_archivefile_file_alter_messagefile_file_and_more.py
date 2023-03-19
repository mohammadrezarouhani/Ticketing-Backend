# Generated by Django 4.1.7 on 2023-03-18 14:22

import auto.path_generator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_rename_history_archive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivefile',
            name='file',
            field=models.FileField(upload_to=auto.path_generator.archive_file_upload),
        ),
        migrations.AlterField(
            model_name='messagefile',
            name='file',
            field=models.FileField(upload_to=auto.path_generator.message_file_upload),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(upload_to=auto.path_generator.profile_image_upload),
        ),
    ]
