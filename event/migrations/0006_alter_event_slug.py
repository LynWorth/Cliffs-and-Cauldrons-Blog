# Generated by Django 4.2.16 on 2024-12-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
