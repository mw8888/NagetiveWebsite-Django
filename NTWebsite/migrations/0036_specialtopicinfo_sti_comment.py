# Generated by Django 2.0.6 on 2018-12-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0035_auto_20181206_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialtopicinfo',
            name='STI_Comment',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
    ]
