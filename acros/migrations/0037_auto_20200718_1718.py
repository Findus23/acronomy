# Generated by Django 3.0.8 on 2020-07-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0036_auto_20200708_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='acronym',
            name='stub',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='historicalacronym',
            name='stub',
            field=models.BooleanField(default=True),
        ),
    ]