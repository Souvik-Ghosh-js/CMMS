# Generated by Django 3.2.18 on 2023-09-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_ticket_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dept',
            field=models.CharField(default=None, max_length=50),
        ),
    ]