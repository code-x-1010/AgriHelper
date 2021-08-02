# Generated by Django 3.2.4 on 2021-06-15 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0002_credentials_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='emp_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                       to='employee.details'),
        ),
    ]
