# Generated by Django 3.2.12 on 2023-01-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]
