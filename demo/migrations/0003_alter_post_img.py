# Generated by Django 4.1 on 2022-11-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='Photos/'),
        ),
    ]
