# Generated by Django 4.1 on 2022-11-13 16:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aegc', '0009_alter_carousel_slug_alter_visa_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='carousel',
            name='subTitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('field', models.CharField(max_length=50)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aegc.social')),
            ],
        ),
    ]
