# Generated by Django 4.2.16 on 2024-09-20 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillset',
            old_name='id',
            new_name='user',
        ),
    ]
