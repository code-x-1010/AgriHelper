# Generated by Django 3.2.4 on 2021-06-16 04:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0005_auto_20210616_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credentials',
            name='status',
        ),
    ]
