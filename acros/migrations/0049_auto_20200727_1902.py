# Generated by Django 3.0.8 on 2020-07-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0048_auto_20200727_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalwikipedialink',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wikipedialink',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]