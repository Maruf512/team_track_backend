# Generated by Django 5.1.2 on 2024-11-01 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_Customer',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Add_Employee',
            new_name='Employee',
        ),
    ]