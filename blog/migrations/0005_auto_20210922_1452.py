# Generated by Django 3.2.7 on 2021-09-22 14:52

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_delete_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-creat_at',), 'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published',), 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creat_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='پست'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('isnotvalid', 'IsNotValid')], default='draft', max_length=10, verbose_name='استاتوس'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ اپدیت'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=models.SET(blog.models.get_sentinel_user), to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creat',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='پابلیش'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=300, unique_for_date='published', verbose_name='پیوند یکتا'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('isnotvalid', 'IsNotValid')], default='draft', max_length=10, verbose_name='استاتوس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='اپدیت'),
        ),
    ]
