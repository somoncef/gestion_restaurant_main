# Generated by Django 4.2.1 on 2023-06-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default='060000000000'),
        ),
    ]
