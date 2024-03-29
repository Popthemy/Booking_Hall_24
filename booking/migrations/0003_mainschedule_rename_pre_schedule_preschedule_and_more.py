# Generated by Django 4.2.6 on 2024-02-14 09:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0002_alter_hall_created_alter_hall_hall_image'),
        ('booking', '0002_main_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSchedule',
            fields=[
                ('start_time', models.PositiveIntegerField(choices=[(7, '7:00 AM'), (8, '8:00 AM'), (9, '9:00 AM'), (10, '10:00 AM'), (11, '11:00 AM'), (12, '12:00 AM'), (13, '1:00 PM'), (14, '2:00 PM'), (15, '3:00 PM'), (16, '4:00 PM'), (17, '5:00 PM'), (18, '6:00 PM'), (19, '7:00 PM')])),
                ('end_time', models.PositiveIntegerField(choices=[(7, '7:00 AM'), (8, '8:00 AM'), (9, '9:00 AM'), (10, '10:00 AM'), (11, '11:00 AM'), (12, '12:00 AM'), (13, '1:00 PM'), (14, '2:00 PM'), (15, '3:00 PM'), (16, '4:00 PM'), (17, '5:00 PM'), (18, '6:00 PM'), (19, '7:00 PM')])),
                ('course_information', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['pre_schedule__date'],
            },
        ),
        migrations.RenameModel(
            old_name='Pre_Schedule',
            new_name='PreSchedule',
        ),
        migrations.DeleteModel(
            name='Main_Schedule',
        ),
        migrations.AddField(
            model_name='mainschedule',
            name='pre_schedule',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.preschedule'),
        ),
        migrations.AlterUniqueTogether(
            name='mainschedule',
            unique_together={('pre_schedule', 'start_time')},
        ),
    ]
