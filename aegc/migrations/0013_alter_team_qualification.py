# Generated by Django 4.1 on 2023-01-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aegc', '0012_rename_field_team_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='qualification',
            field=models.CharField(max_length=100),
        ),
    ]