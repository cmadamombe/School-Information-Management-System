# Generated by Django 3.0.5 on 2020-04-18 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='schoolprofile',
            name='modified_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
    ]