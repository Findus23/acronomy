# Generated by Django 3.0.8 on 2020-07-19 19:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0045_auto_20200719_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acronym',
            name='acro_letters',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='historicalacronym',
            name='acro_letters',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, null=True, size=None),
        ),
    ]
