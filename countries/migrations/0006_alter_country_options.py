# Generated by Django 4.1.6 on 2023-02-16 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_alter_country_capital'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]
