# Generated by Django 5.1.2 on 2024-11-09 07:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_viewcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
