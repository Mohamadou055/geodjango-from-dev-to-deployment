# Generated by Django 3.2.9 on 2021-11-28 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shp',
            old_name='files',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='shp',
            name='uploaded_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
