# Generated by Django 2.0.6 on 2018-12-26 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0044_auto_20181225_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationtable',
            old_name='NT_Sign',
            new_name='NT_Part',
        ),
        migrations.RenameField(
            model_name='notificationtable',
            old_name='NT_Plate',
            new_name='NT_URL',
        ),
    ]
