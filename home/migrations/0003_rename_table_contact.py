# Generated by Django 4.1.1 on 2022-10-01 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contact_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='table',
            new_name='contact',
        ),
    ]
