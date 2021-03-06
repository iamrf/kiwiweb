# Generated by Django 3.0 on 2019-12-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
