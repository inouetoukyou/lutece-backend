# Generated by Django 2.0.4 on 2018-05-08 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20180508_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersolveinfo',
            name='problem',
        ),
        migrations.RemoveField(
            model_name='usersolveinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Usersolveinfo',
        ),
    ]