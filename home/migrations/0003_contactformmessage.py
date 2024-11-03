# Generated by Django 5.1.2 on 2024-11-03 08:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_setings_aboutus_alter_setings_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=150)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=15)),
                ('notes', ckeditor_uploader.fields.RichTextUploadingField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
