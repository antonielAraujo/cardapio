# Generated by Django 4.2.4 on 2023-12-01 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 21, 11, 23, 372319)),
        ),
    ]
