# Generated by Django 3.2.18 on 2023-09-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user_hid',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user_uid',
        ),
        migrations.AddField(
            model_name='ticket',
            name='HID',
            field=models.CharField(default=' ', max_length=10),
        ),
        migrations.AddField(
            model_name='ticket',
            name='UID',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='facilities',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
