# Generated by Django 3.1.3 on 2023-02-16 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trains', '0002_auto_20230215_2108'),
        ('cities', '0002_auto_20230214_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route name')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Total travel time')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='From what city?')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='Which city?')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='List of trains')),
            ],
        ),
    ]
