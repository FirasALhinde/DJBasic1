# Generated by Django 3.2 on 2022-12-30 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]