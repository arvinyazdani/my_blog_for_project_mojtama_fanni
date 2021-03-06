# Generated by Django 3.2.7 on 2021-09-16 08:57

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('isnotvalid', 'IsNotValid')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-creat_at',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('sen', models.SmallIntegerField()),
                ('id_number', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=11)),
                ('bio', models.TextField(blank=True)),
                ('gener', models.BooleanField()),
                ('is_writor', models.BooleanField()),
                ('file_resome', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('image', models.CharField(max_length=10)),
                ('author', models.CharField(max_length=10)),
                ('slug', models.CharField(max_length=300, unique_for_date='published')),
                ('creat', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('isnotvalid', 'IsNotValid')], default='draft', max_length=10)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
