# Generated by Django 3.0.6 on 2020-05-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0015_auto_20200531_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipedialink',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='wikipedia_thumbnails/'),
        ),
    ]
