# Generated by Django 3.1.5 on 2021-03-16 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210316_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='first_name',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='user_info',
            old_name='last_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='phone',
        ),
    ]
