# Generated by Django 2.0.6 on 2018-12-04 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0020_auto_20181203_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialtopicinfo',
            name='STI_Cover',
        ),
    ]