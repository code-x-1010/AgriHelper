# Generated by Django 3.2.4 on 2021-06-16 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0006_remove_credentials_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.details')),
            ],
        ),
    ]
