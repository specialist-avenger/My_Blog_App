# Generated by Django 4.0.5 on 2022-06-30 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_posts_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='title_image',
        ),
    ]
