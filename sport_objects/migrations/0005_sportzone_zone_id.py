# Generated by Django 3.1.7 on 2021-10-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_objects', '0004_auto_20211011_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportzone',
            name='zone_id',
            field=models.TextField(null=True),
        ),
    ]
