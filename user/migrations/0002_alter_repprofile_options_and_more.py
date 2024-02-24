# Generated by Django 4.2.6 on 2024-02-22 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repprofile',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='repprofile',
            old_name='contatct_info',
            new_name='contact_info',
        ),
        migrations.AlterField(
            model_name='repprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='repprofile',
            name='level',
            field=models.CharField(blank=True, choices=[(100, '100L'), (200, '200L'), (300, '300L'), (400, '400L'), (500, '500L'), (600, '600L'), (700, '700L')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='repprofile',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repprofile',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
