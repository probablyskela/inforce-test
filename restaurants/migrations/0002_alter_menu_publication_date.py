# Generated by Django 4.2.4 on 2023-08-12 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='publication_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]