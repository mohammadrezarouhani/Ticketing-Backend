# Generated by Django 4.1.7 on 2023-03-18 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0006_alter_archivefile_file_alter_messagefile_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivefile',
            old_name='history',
            new_name='archive',
        ),
        migrations.RenameField(
            model_name='messagefile',
            old_name='comment',
            new_name='message',
        ),
    ]
