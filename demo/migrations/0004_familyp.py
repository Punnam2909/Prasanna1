# Generated by Django 4.1 on 2022-11-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_alter_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='familyp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('DOB', models.DateField()),
            ],
            options={
                'verbose_name': 'familyp',
                'verbose_name_plural': 'familyps',
            },
        ),
    ]
