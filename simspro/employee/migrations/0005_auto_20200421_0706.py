# Generated by Django 3.0.5 on 2020-04-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200421_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employee_number',
            field=models.IntegerField(blank=True, default='23324383', editable=False, unique=True, verbose_name='Employee Number'),
        ),
    ]
