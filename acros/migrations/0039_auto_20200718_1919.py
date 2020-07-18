# Generated by Django 3.0.8 on 2020-07-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0038_auto_20200718_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikipediaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('pageid', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='wikipedia_thumbnails/')),
                ('thumb_width', models.IntegerField(blank=True, editable=False, null=True)),
                ('thumb_height', models.IntegerField(blank=True, editable=False, null=True)),
                ('imageurl', models.URLField()),
                ('caption', models.CharField(blank=True, max_length=1000, null=True)),
                ('credit', models.TextField()),
                ('artist', models.TextField()),
                ('license_short_name', models.TextField()),
                ('attribution', models.TextField()),
                ('license_url', models.URLField()),
                ('attribution_required', models.BooleanField()),
                ('copyrighted', models.BooleanField()),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='historicalwikipedialink',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='historicalwikipedialink',
            name='thumbnail_caption',
        ),
        migrations.RemoveField(
            model_name='historicalwikipedialink',
            name='thumbnail_height',
        ),
        migrations.RemoveField(
            model_name='historicalwikipedialink',
            name='thumbnail_title',
        ),
        migrations.RemoveField(
            model_name='historicalwikipedialink',
            name='thumbnail_width',
        ),
        migrations.RemoveField(
            model_name='wikipedialink',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='wikipedialink',
            name='thumbnail_caption',
        ),
        migrations.RemoveField(
            model_name='wikipedialink',
            name='thumbnail_height',
        ),
        migrations.RemoveField(
            model_name='wikipedialink',
            name='thumbnail_title',
        ),
        migrations.RemoveField(
            model_name='wikipedialink',
            name='thumbnail_width',
        ),
    ]
