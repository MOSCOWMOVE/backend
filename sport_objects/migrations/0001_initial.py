# Generated by Django 3.2.8 on 2021-10-10 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('distance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentalOrganisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('dep_id', models.UUIDField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SportZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('accessibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_objects.accessibility')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_objects.departmentalorganisation')),
                ('sportTypes', models.ManyToManyField(to='sport_objects.SportType')),
            ],
        ),
    ]
