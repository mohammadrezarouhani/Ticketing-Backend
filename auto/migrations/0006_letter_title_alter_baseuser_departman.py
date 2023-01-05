# Generated by Django 4.1.3 on 2023-01-05 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_rename_discription_departman_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='title',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='departman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departman_detail', to='auto.departman'),
        ),
    ]