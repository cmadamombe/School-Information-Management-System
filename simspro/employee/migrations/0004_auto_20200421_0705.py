# Generated by Django 3.0.5 on 2020-04-21 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0006_title'),
        ('employee', '0003_auto_20200421_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Nationality', verbose_name='Nationality'),
        ),
        migrations.AddField(
            model_name='employees',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Qualification', verbose_name='Highest Qualification'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employee_number',
            field=models.IntegerField(blank=True, default='27397790', editable=False, unique=True, verbose_name='Employee Number'),
        ),
    ]