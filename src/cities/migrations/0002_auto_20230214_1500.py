# Generated by Django 3.1.3 on 2023-02-14 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
    ]
