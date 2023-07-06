# Generated by Django 4.2.2 on 2023-07-05 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0006_alter_loan_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 15, 11, 14, 807624, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]
