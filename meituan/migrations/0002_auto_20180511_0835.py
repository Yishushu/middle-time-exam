# Generated by Django 2.0.1 on 2018-05-11 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='address',
            new_name='Order',
        ),
    ]