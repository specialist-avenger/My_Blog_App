# Generated by Django 4.0.5 on 2022-06-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_posts_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='title_tag',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
