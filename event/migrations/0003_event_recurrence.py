# Generated by Django 4.2.16 on 2024-12-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_options_event_capacity_event_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='recurrence',
            field=models.CharField(choices=[('none', 'None'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('yearly', 'Yearly')], default='none', max_length=20),
        ),
    ]