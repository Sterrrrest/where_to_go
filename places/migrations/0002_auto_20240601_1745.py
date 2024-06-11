# Generated by Django 3.2.25 on 2024-06-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='detailsUrl',
            field=models.CharField(blank=True, max_length=50, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='place',
            name='geo_title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название на карте'),
        ),
        migrations.AddField(
            model_name='place',
            name='placeId',
            field=models.CharField(blank=True, max_length=50, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='longitude'),
        ),
    ]
