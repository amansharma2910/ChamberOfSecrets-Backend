# Generated by Django 2.2.19 on 2021-03-25 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'managed': False, 'ordering': ['user_id']},
        ),
    ]
