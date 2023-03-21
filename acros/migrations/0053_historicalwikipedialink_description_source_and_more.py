# Generated by Django 4.1.7 on 2023-03-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("acros", "0052_historicalwikipedialink_wikibase_item_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalwikipedialink",
            name="description_source",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="wikipedialink",
            name="description_source",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]