# Generated by Django 4.0.5 on 2022-07-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_posts_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='article_snippet',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
