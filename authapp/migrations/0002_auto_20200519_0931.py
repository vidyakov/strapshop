# Generated by Django 3.0.6 on 2020-05-19 09:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strapuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='strapuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 9, 51, 2, 3753, tzinfo=utc)),
        ),
    ]
