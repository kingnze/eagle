# Generated by Django 4.1.7 on 2023-03-03 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eagles', '0003_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 3, 11, 19, 12, 603983)),
        ),
    ]
