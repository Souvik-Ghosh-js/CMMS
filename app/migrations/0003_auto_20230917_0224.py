# Generated by Django 3.2.18 on 2023-09-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230916_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='hname',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='hreason',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(default='Sent', max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='time',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='uname',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='hname',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]