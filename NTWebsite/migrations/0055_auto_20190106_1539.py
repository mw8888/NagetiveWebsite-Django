# Generated by Django 2.0.6 on 2019-01-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NTWebsite', '0054_auto_20190103_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configparams',
            name='CP_CommentsLimit',
            field=models.CharField(default=100, max_length=20, verbose_name='文章评论获取数量'),
        ),
        migrations.AlterField(
            model_name='configparams',
            name='CP_ReadsThreshold',
            field=models.CharField(default=10, max_length=20, verbose_name='上榜阅读量'),
        ),
        migrations.AlterField(
            model_name='configparams',
            name='CP_TopicsLimit',
            field=models.CharField(default=100, max_length=20, verbose_name='文章获取数量'),
        ),
    ]