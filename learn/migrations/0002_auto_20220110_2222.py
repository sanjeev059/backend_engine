# Generated by Django 2.2 on 2022-01-10 16:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createtask',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createtask',
            name='state',
            field=models.CharField(default=datetime.datetime(2022, 1, 10, 16, 52, 7, 590790, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
