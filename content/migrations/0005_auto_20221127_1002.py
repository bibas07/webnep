# Generated by Django 2.2.12 on 2022-11-27 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20221127_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_name',
        ),
    ]
