# Generated by Django 2.0.6 on 2018-12-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0048_auto_20181228_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationtable',
            name='NT_AnchorID',
            field=models.CharField(default='', max_length=100, verbose_name='定位ID'),
        ),
    ]