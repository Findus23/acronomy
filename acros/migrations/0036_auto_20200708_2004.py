# Generated by Django 3.0.8 on 2020-07-08 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0035_acrooftheday_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acrooftheday',
            options={'ordering': ['date', 'order']},
        ),
    ]
