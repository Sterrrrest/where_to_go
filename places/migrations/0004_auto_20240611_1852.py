# Generated by Django 3.2.25 on 2024-06-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='detailsUrl',
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='Позиция'),
        ),
    ]
