# Generated by Django 4.2.6 on 2024-02-22 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_mainschedule_rename_pre_schedule_preschedule_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainschedule',
            options={'ordering': ['-pre_schedule__date']},
        ),
    ]
