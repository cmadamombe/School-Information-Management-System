# Generated by Django 3.0.5 on 2020-05-12 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parents',
            options={'ordering': ('user',), 'verbose_name': 'Parent Profile', 'verbose_name_plural': 'Parents Profile'},
        ),
        migrations.RemoveField(
            model_name='parents',
            name='p_id',
        ),
    ]
