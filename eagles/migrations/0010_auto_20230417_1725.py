# Generated by Django 3.2.5 on 2023-04-17 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagles', '0009_auto_20230417_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 17, 17, 25, 16, 84478)),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
