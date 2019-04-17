# Generated by Django 2.2 on 2019-04-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tasker_unisender', '0009_auto_20190417_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email address')),
                ('list', models.ManyToManyField(to='django_tasker_unisender.List')),
            ],
            options={
                'verbose_name': 'Subscribe',
                'verbose_name_plural': 'Subscribes',
            },
        ),
    ]
