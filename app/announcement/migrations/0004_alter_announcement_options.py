# Generated by Django 4.0.1 on 2022-01-29 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_announcement_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['-id']},
        ),
    ]
