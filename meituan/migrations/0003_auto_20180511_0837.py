# Generated by Django 2.0.1 on 2018-05-11 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0002_auto_20180511_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='meal',
        ),
    ]
