# Generated by Django 3.1.5 on 2021-02-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210218_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='birth_date'),
        ),
    ]
