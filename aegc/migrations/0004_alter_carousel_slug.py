# Generated by Django 4.1 on 2022-09-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aegc', '0003_alter_carousel_image_alter_carousel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
