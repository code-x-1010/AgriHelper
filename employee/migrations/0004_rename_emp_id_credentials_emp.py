# Generated by Django 3.2.4 on 2021-06-16 04:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0003_alter_credentials_emp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credentials',
            old_name='emp_id',
            new_name='emp',
        ),
    ]
