# Generated by Django 4.2.1 on 2023-06-18 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=datetime.time(13, 12, 43, 670283)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='nbrpersonne',
            field=models.IntegerField(),
        ),
    ]