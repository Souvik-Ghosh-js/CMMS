# Generated by Django 3.2.18 on 2023-09-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UID',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
