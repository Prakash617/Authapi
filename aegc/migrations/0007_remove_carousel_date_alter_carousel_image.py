# Generated by Django 4.1 on 2022-09-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aegc', '0006_carousel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='date',
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/Carusel'),
        ),
    ]
