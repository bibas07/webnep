# Generated by Django 3.2.12 on 2023-02-07 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_document_aurthur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png', 'gif'])]),
        ),
    ]
