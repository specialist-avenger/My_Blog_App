# Generated by Django 4.0.5 on 2022-09-06 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_profile_pintrest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='images/profile/%y%m%d'),
        ),
    ]
