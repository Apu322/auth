# Generated by Django 3.2.7 on 2022-06-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=100),
        ),
    ]
