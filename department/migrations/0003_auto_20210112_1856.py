# Generated by Django 3.1.5 on 2021-01-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_department_mgr_ssn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dnumber',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]