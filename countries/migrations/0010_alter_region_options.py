# Generated by Django 4.1.6 on 2023-02-16 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0009_alter_country_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['name']},
        ),
    ]
