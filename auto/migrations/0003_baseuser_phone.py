# Generated by Django 4.1.3 on 2022-12-26 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_comment_remove_departman_user_baseuser_departman_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='phone',
            field=models.CharField(default='+914000000', max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]