# Generated by Django 2.0.6 on 2018-12-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0024_auto_20181204_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialtopicinfo',
            name='STI_Cover',
            field=models.ImageField(default='', upload_to='Cover', verbose_name='封面'),
        ),
    ]