# Generated by Django 3.1.7 on 2021-05-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20210518_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='d',
        ),
    ]
