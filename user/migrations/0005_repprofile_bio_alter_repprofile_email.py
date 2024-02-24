# Generated by Django 4.2.6 on 2024-02-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_repprofile_contact_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='repprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='repprofile',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
