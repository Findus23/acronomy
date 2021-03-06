# Generated by Django 3.0.6 on 2020-05-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0008_auto_20200528_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='extract',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='extract_html',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail_height',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='thumbnail_width',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalwikipedialink',
            name='timestamp',
            field=models.DateTimeField(default='2020-01-01 00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='extract',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='extract_html',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail',
            field=models.FileField(blank=True, upload_to='wikipedia_thumbnails/'),
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail_height',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='thumbnail_width',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikipedialink',
            name='timestamp',
            field=models.DateTimeField(default='2020-01-01 00:00'),
            preserve_default=False,
        ),
    ]
