# Generated by Django 3.0.6 on 2020-06-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0025_auto_20200601_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail_caption',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail_caption',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
