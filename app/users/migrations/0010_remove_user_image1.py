# Generated by Django 4.0.1 on 2022-01-31 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image1',
        ),
    ]
