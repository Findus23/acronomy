# Generated by Django 3.0.6 on 2020-05-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acros', '0007_auto_20200528_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
