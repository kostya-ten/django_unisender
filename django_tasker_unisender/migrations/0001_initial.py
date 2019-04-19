# Generated by Django 2.2 on 2019-04-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('emailmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_tasker_unisender.EmailModel')),
            ],
            bases=('django_tasker_unisender.emailmodel',),
        ),
        migrations.CreateModel(
            name='SubscribeTest',
            fields=[
                ('emailmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_tasker_unisender.EmailModel')),
            ],
            bases=('django_tasker_unisender.emailmodel',),
        ),
    ]
