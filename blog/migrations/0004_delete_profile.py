# Generated by Django 3.2.7 on 2021-09-19 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
