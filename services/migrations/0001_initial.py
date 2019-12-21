# Generated by Django 3.0 on 2019-12-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, verbose_name='Slug')),
                ('template', models.CharField(max_length=200, verbose_name='Template')),
                ('domain', models.CharField(max_length=200, verbose_name='Domain')),
                ('host', models.CharField(max_length=200, verbose_name='Host')),
                ('support', models.CharField(blank=True, max_length=200, verbose_name='Support')),
                ('op_1', models.CharField(blank=True, max_length=200, verbose_name='Option 1')),
                ('op_2', models.CharField(blank=True, max_length=200, verbose_name='Option 2')),
                ('op_3', models.CharField(blank=True, max_length=200, verbose_name='Option 3')),
                ('op_4', models.CharField(blank=True, max_length=200, verbose_name='Option 4')),
                ('op_5', models.CharField(blank=True, max_length=200, verbose_name='Option 5')),
                ('op_6', models.CharField(blank=True, max_length=200, verbose_name='Option 6')),
                ('op_7', models.CharField(blank=True, max_length=200, verbose_name='Option 7')),
                ('op_8', models.CharField(blank=True, max_length=200, verbose_name='Option 8')),
                ('op_9', models.CharField(blank=True, max_length=200, verbose_name='Option 9')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.CharField(max_length=50, verbose_name='Price')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='Sorting')),
                ('publish', models.BooleanField(default=True, verbose_name='Publish')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
