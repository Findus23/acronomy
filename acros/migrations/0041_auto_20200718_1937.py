# Generated by Django 3.0.8 on 2020-07-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0040_auto_20200718_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipediaimage',
            name='attribution',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='license_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
