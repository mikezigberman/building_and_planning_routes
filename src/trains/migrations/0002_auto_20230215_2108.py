# Generated by Django 3.1.3 on 2023-02-15 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20230214_1500'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traintest',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.city', verbose_name='From what city?'),
        ),
    ]
