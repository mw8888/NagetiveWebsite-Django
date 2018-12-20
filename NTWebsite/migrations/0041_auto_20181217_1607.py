# Generated by Django 2.0.6 on 2018-12-17 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0040_notificationtable_nt_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlink',
            name='UL_UserBeLinked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='被关注用户'),
        ),
        migrations.AlterField(
            model_name='userlink',
            name='UL_UserLinking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserNameLinking', to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='关注用户'),
        ),
    ]