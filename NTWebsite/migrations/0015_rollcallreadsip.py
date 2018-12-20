# Generated by Django 2.0.6 on 2018-11-26 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0014_rollcallinfo_rci_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='RollCallReadsIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RCR_IP', models.CharField(blank=True, max_length=100, null=True, verbose_name='IP')),
                ('RCR_EditDate', models.DateField(auto_now=True, verbose_name='时间')),
                ('RCR_ArticleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.RollCallInfo', to_field='RCI_Title', verbose_name='围观ID')),
            ],
            options={
                'verbose_name_plural': '围观阅读IP统计',
            },
        ),
    ]
