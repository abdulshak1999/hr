# Generated by Django 3.1.5 on 2021-01-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ssn',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]