# Generated by Django 3.2.18 on 2023-09-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_ticket_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin1',
            field=models.BooleanField(default=False, verbose_name='Is superadmin'),
        ),
    ]
