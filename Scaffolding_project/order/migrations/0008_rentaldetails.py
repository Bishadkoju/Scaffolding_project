# Generated by Django 2.2.12 on 2020-05-13 03:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200512_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateField(default=datetime.datetime.now)),
                ('expected_duration', models.PositiveIntegerField()),
                ('returned_date', models.DateField()),
                ('order_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderRegister')),
            ],
        ),
    ]
