# Generated by Django 4.1.7 on 2023-02-25 12:45

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=500)),
                ('title_2', models.CharField(max_length=500)),
                ('title_3', models.CharField(max_length=500)),
                ('title_4', models.CharField(max_length=500)),
                ('text_1', models.TextField(blank=True)),
                ('text_2', models.TextField(blank=True)),
                ('text_3', models.TextField(blank=True)),
                ('text_4', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=True, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2023, 2, 25, 13, 45, 7, 724106))),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'db_table': 'Blog',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=200)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('request_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Bookings',
                'verbose_name_plural': 'Bookings',
                'db_table': 'Booking',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comfort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True)),
                ('diningimg', models.ImageField(upload_to='')),
                ('text_1', models.CharField(blank=True, max_length=500, null=True)),
                ('text_2', models.CharField(blank=True, max_length=500, null=True)),
                ('text_3', models.CharField(blank=True, max_length=500, null=True)),
                ('text_4', models.CharField(blank=True, max_length=500, null=True)),
                ('text_5', models.CharField(blank=True, max_length=500, null=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Dining',
                'verbose_name_plural': 'Dining',
                'db_table': 'Dining',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imggallery', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Gallerys',
                'verbose_name_plural': 'Gallerys',
                'db_table': 'gallery',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('meetimg', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Meetings',
                'verbose_name_plural': 'Meetings',
                'db_table': 'meeting',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ourinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('years', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=500)),
                ('subtitle_1', models.CharField(max_length=500)),
                ('subtitle_2', models.CharField(max_length=500)),
                ('text_1', models.TextField(blank=True)),
                ('text_2', models.TextField(blank=True)),
                ('leadimg', models.ImageField(blank=True, default='myleadimg.jpg', null=True, upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Ourinfo',
                'verbose_name_plural': 'Ourinfo',
                'db_table': 'Ourinfo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ourservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Ourservice1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('subtitle_1', models.CharField(max_length=500)),
                ('subtitle_2', models.CharField(max_length=500)),
                ('text_1', models.TextField(blank=True)),
                ('text_2', models.TextField(blank=True)),
                ('leadimg', models.ImageField(blank=True, default='myleadimg.jpg', null=True, upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('guests', models.CharField(blank=True, max_length=50)),
                ('bed', models.CharField(blank=True, max_length=50)),
                ('car_rent', models.CharField(blank=True, max_length=50, null=True)),
                ('roomimg', models.ImageField(upload_to='')),
                ('roomimg1', models.ImageField(blank=True, upload_to='')),
                ('roomtmg2', models.ImageField(blank=True, upload_to='')),
                ('roomtmg3', models.ImageField(blank=True, upload_to='')),
                ('roomtmg4', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('isbooked', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'rooms',
                'verbose_name_plural': 'rooms',
                'db_table': 'room',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=500)),
                ('title_2', models.CharField(max_length=500)),
                ('title_3', models.CharField(max_length=500)),
                ('title_4', models.CharField(max_length=500)),
                ('title_5', models.CharField(max_length=500)),
                ('title_6', models.CharField(max_length=500)),
                ('subtitle_1', models.CharField(max_length=500)),
                ('subtitle_2', models.CharField(max_length=500)),
                ('subtitle_3', models.CharField(max_length=500)),
                ('subtitle_4', models.CharField(max_length=500)),
                ('subtitle_5', models.CharField(max_length=500)),
                ('text_1', models.TextField(blank=True)),
                ('text_2', models.TextField(blank=True)),
                ('text_3', models.TextField(blank=True)),
                ('text_4', models.TextField(blank=True)),
                ('text_5', models.TextField(blank=True)),
                ('text_6', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('spaimg', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Spa',
                'verbose_name_plural': 'Spa',
                'db_table': 'spa',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Whoweare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('text_1', models.CharField(max_length=500)),
                ('text_2', models.CharField(max_length=500)),
                ('text_3', models.CharField(max_length=500)),
                ('text_4', models.CharField(max_length=500)),
                ('text_5', models.CharField(max_length=500)),
                ('text_6', models.CharField(max_length=500)),
                ('leadimg', models.ImageField(blank=True, default='myleadimg.jpg', null=True, upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('published', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Whoweare',
                'verbose_name_plural': 'Whoweare',
                'db_table': 'Whoweare',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Blogusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eagles.blog')),
            ],
            options={
                'verbose_name': 'BlogComment',
                'verbose_name_plural': 'BlogComments',
                'db_table': 'BlogComments',
                'managed': True,
            },
        ),
    ]