# Generated by Django 3.2.8 on 2021-10-19 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_auto_20211019_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pinterest_url',
            new_name='youtube_url',
        ),
    ]
