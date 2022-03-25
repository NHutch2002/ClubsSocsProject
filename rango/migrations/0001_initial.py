# Generated by Django 2.2.26 on 2022-03-22 13:42

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_society', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, upload_to='profile_pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('societyName', models.CharField(max_length=64, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='society_logos')),
                ('description', models.CharField(max_length=256)),
                ('views', models.IntegerField(default=0)),
                ('memberNum', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('member', models.ManyToManyField(null=True, related_name='memberOf', to='rango.UserProfile')),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rango.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Societies',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('memberNum', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date(2022, 3, 22))),
                ('slug', models.SlugField(unique=True)),
                ('attendee', models.ManyToManyField(null=True, to='rango.UserProfile')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Society')),
            ],
        ),
    ]
