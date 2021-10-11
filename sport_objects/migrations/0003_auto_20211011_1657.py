# Generated by Django 3.1.7 on 2021-10-11 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_objects', '0002_auto_20211010_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.FloatField()),
                ('longittude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='sportzone',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sport_objects.position'),
        ),
    ]
