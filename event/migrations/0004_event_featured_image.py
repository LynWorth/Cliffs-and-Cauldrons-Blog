# Generated by Django 4.2.16 on 2024-12-03 12:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_recurrence'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
