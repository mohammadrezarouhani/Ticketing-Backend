# Generated by Django 4.1.3 on 2022-11-23 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0006_alter_baseuser_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketmessage',
            old_name='reciever',
            new_name='receiver',
        ),
    ]
