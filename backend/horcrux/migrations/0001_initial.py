# Generated by Django 2.2.19 on 2021-03-25 10:04

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
            name='FileData',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=1024)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['file_id'],
                'unique_together': {('user_id', 'file_id')},
            },
        ),
        migrations.CreateModel(
            name='FileParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_1', models.URLField()),
                ('split_2', models.URLField()),
                ('split_3', models.URLField()),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horcrux.FileData')),
            ],
        ),
    ]
