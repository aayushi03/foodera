# Generated by Django 2.1.1 on 2018-10-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_list',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
