# Generated by Django 2.0.4 on 2018-04-14 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_auto_20180414_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['problem_id']},
        ),
    ]