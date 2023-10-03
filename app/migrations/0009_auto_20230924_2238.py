# Generated by Django 3.2.18 on 2023-09-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_is_admin1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin1',
            new_name='is_superadmin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='user',
            name='facility',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='is_GMAadmin',
            field=models.BooleanField(default=False, verbose_name='Is GMAadmin'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_SYSadmin',
            field=models.BooleanField(default=False, verbose_name='Is SYSadmin'),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
