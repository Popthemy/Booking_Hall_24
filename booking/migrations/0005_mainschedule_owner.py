# Generated by Django 4.2.6 on 2024-02-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('booking', '0004_alter_mainschedule_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainschedule',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.repprofile'),
        ),
    ]
