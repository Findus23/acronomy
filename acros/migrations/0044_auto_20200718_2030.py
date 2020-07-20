# Generated by Django 3.0.8 on 2020-07-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0043_auto_20200718_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikipediaimage',
            name='artist',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='attribution',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='attribution_required',
            field=models.BooleanField(editable=False),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='copyrighted',
            field=models.BooleanField(editable=False),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='credit',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='imageurl',
            field=models.URLField(editable=False),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='license_short_name',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='license_url',
            field=models.URLField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='pageid',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='wikipedia_images/'),
        ),
        migrations.AlterField(
            model_name='wikipediaimage',
            name='timestamp',
            field=models.DateTimeField(blank=True, editable=False),
        ),
    ]