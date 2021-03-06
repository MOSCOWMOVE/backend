# Generated by Django 3.1.7 on 2021-10-14 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_objects', '0005_sportzone_zone_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='sportzone',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sportzone',
            name='square',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='sportzone',
            name='open_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport_objects.openedtype'),
        ),
    ]
