# Generated by Django 4.1 on 2022-09-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aegc', '0004_alter_carousel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
