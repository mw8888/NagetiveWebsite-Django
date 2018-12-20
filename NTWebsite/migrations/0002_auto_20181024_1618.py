# Generated by Django 2.0.6 on 2018-10-24 08:18

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('NTWebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('AC_ID', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='评论ID')),
                ('AC_Comment', models.TextField(verbose_name='评论内容')),
                ('AC_Parent', models.UUIDField(blank=True, null=True, verbose_name='父评论')),
                ('AC_Likes', models.IntegerField(default='0', verbose_name='赞')),
                ('AC_Dislikes', models.IntegerField(default='0', verbose_name='怼')),
                ('AC_EditDate', models.DateTimeField(auto_now=True, verbose_name='编辑时间')),
                ('AC_Readstatus', models.CharField(choices=[('Y', '已阅'), ('N', '未读')], default='N', max_length=1, verbose_name='是否阅读')),
            ],
            options={
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='ArticleReadsIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AR_IP', models.CharField(blank=True, max_length=100, null=True, verbose_name='IP')),
                ('AR_EditDate', models.DateField(auto_now=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '阅读IP统计',
            },
        ),
        migrations.CreateModel(
            name='ArticleTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AT_TAID', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='文章ID')),
                ('AT_ID', models.IntegerField(verbose_name='标签代码')),
                ('AT_Name', models.CharField(max_length=10, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='ArticleUserLikesOrDislikesTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ALD_StandPoint', models.IntegerField(verbose_name='立场代码')),
                ('ALD_EditDate', models.DateField(auto_now=True, verbose_name='时间')),
            ],
            options={
                'verbose_name_plural': '立场统计',
            },
        ),
        migrations.CreateModel(
            name='CategoryInfo',
            fields=[
                ('CI_Name', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='品类名称')),
                ('CI_SVG', models.TextField(max_length=1000, verbose_name='图标SVG')),
            ],
            options={
                'verbose_name_plural': '品类',
            },
        ),
        migrations.CreateModel(
            name='ConfigParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CP_Name', models.CharField(max_length=20, unique=True, verbose_name='配置名称')),
                ('CP_ReadsThreshold', models.IntegerField(default=10, verbose_name='上榜阅读量')),
                ('CP_HotKeyWord', models.CharField(default='差评', max_length=20, verbose_name='热搜关键字')),
                ('CP_TopicsLimit', models.IntegerField(default=100, verbose_name='文章获取数量')),
                ('CP_CommentsLimit', models.IntegerField(default=100, verbose_name='文章评论获取数量')),
                ('CP_SecretKey', models.CharField(max_length=16, verbose_name='加密秘钥')),
                ('CP_SecretVI', models.CharField(max_length=16, verbose_name='加密偏移量')),
                ('CP_TopicsPageLimit', models.IntegerField(default=10, verbose_name='每页文章数量')),
                ('CP_CommentsPageLimit', models.IntegerField(default=10, verbose_name='每页评论数量')),
                ('CP_AvatarResolution', models.IntegerField(default=102, verbose_name='头像分辨率')),
            ],
            options={
                'verbose_name_plural': '配置参数',
            },
        ),
        migrations.CreateModel(
            name='PreferredConfigName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PC_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.ConfigParams', to_field='CP_Name', verbose_name='首选配置名称')),
            ],
            options={
                'verbose_name_plural': '首选配置设置',
            },
        ),
        migrations.CreateModel(
            name='TopicArticleStatistic',
            fields=[
                ('TAS_ID', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='文章ID')),
                ('TAS_Title', models.CharField(max_length=35, unique=True, verbose_name='文章标题')),
                ('TAS_Description', models.TextField(max_length=140, verbose_name='文章描述')),
                ('TAS_EditDate', models.DateField(auto_now=True, verbose_name='编辑时间')),
                ('TAS_Theme', models.CharField(default='其他', max_length=100, verbose_name='文章主题')),
                ('TAS_Like', models.IntegerField(default=0, verbose_name='赞')),
                ('TAS_Dislike', models.IntegerField(default=0, verbose_name='怼')),
                ('TAS_Read', models.IntegerField(default=10, verbose_name='阅读量')),
                ('TAS_Comment', models.IntegerField(default=0, verbose_name='评论数')),
                ('TAS_Content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='文章正文')),
            ],
            options={
                'verbose_name_plural': '文章信息',
            },
        ),
        migrations.CreateModel(
            name='TopicArticleTheme',
            fields=[
                ('TAT_ID', models.CharField(default='0', max_length=10, primary_key=True, serialize=False, verbose_name='主题代码')),
                ('TAT_Name', models.CharField(max_length=10, unique=True, verbose_name='主题名称')),
            ],
            options={
                'verbose_name_plural': '主题',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('UT_Nick', models.CharField(max_length=20, verbose_name='昵称')),
                ('UT_Sex', models.CharField(blank=True, default='未公开', max_length=3, verbose_name='性别')),
                ('UT_Region', models.CharField(blank=True, default='城市', max_length=10, null=True, verbose_name='地区')),
                ('UT_Description', models.TextField(blank=True, default='简介', max_length=50, null=True, verbose_name='简介')),
                ('UT_Avatar', models.TextField(blank=True, default='/static/media/DefaultLogo.jpg', max_length=1000, verbose_name='头像URL')),
                ('UT_Constellation', models.CharField(blank=True, default='天蝎座', max_length=10, null=True, verbose_name='星座')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='topicarticlestatistic',
            name='TAS_Author',
            field=models.ForeignKey(default='flysafely', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='topicarticlestatistic',
            name='TAS_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.CategoryInfo', verbose_name='文章类别'),
        ),
        migrations.AddField(
            model_name='articleuserlikesordislikestable',
            name='ALD_ArticleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.TopicArticleStatistic', to_field='TAS_Title', verbose_name='文章ID'),
        ),
        migrations.AddField(
            model_name='articleuserlikesordislikestable',
            name='ALD_UserNickName',
            field=models.ForeignKey(default='flysafely', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='articlereadsip',
            name='AR_ArticleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.TopicArticleStatistic', to_field='TAS_Title', verbose_name='文章ID'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='AC_ArticleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NTWebsite.TopicArticleStatistic', to_field='TAS_Title', verbose_name='文章ID'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='AC_UserNickName',
            field=models.ForeignKey(default='flysafely', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', verbose_name='用户名'),
        ),
    ]
