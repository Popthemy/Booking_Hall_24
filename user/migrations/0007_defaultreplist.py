# Generated by Django 4.2.6 on 2024-02-28 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_repprofile_i_am_a_rep'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultRepList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=250)),
            ],
        ),
    ]
