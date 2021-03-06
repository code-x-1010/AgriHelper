# Generated by Django 3.2.4 on 2021-06-16 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('cust_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField(unique=True)),
                ('aadhar_no', models.IntegerField(unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('cust',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='customer.details')),
                ('password', models.CharField(max_length=32)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
