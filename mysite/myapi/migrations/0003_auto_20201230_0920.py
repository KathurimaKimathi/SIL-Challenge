# Generated by Django 3.1.4 on 2020-12-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20201230_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
    ]
