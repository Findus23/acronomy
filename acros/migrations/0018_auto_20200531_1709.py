# Generated by Django 3.0.6 on 2020-05-31 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0017_auto_20200531_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail_height',
            field=models.IntegerField(blank=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail_width',
            field=models.IntegerField(blank=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail_height',
            field=models.IntegerField(blank=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail_width',
            field=models.IntegerField(blank=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]
