# Generated by Django 3.2.7 on 2021-10-01 14:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_person_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 1, 14, 48, 24, 584749, tzinfo=utc)),
        ),
    ]
