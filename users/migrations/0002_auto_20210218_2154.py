# Generated by Django 3.1.5 on 2021-02-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(verbose_name='birth_date'),
        ),
    ]
