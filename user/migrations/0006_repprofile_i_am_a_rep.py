# Generated by Django 4.2.6 on 2024-02-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_repprofile_bio_alter_repprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='repprofile',
            name='i_am_a_rep',
            field=models.BooleanField(default=False),
        ),
    ]