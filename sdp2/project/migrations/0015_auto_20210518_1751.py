# Generated by Django 3.1.7 on 2021-05-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20210518_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorregister',
            name='maxappointments',
            field=models.IntegerField(),
        ),
    ]