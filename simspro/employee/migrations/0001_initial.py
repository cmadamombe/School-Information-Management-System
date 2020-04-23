# Generated by Django 3.0.5 on 2020-04-21 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setup', '0006_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300, verbose_name='First Name')),
                ('other_name', models.CharField(max_length=300, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=300, verbose_name='Last Name')),
                ('employee_number', models.IntegerField(blank=True, default='43495128', editable=False, unique=True, verbose_name='Employee Number')),
                ('employee_email', models.EmailField(blank=True, max_length=500, verbose_name='Employee Email')),
                ('employee_phone', models.CharField(max_length=12, verbose_name='Employee Phone')),
                ('date_of_joining', models.DateField(verbose_name='Date Joined')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Physical Address')),
                ('teacher_profile_summary', models.TextField(blank=True, null=True, verbose_name='Employee Profile Summary')),
                ('profile_image', models.ImageField(blank=True, upload_to='images/', verbose_name='Profile Image')),
                ('spouse_name', models.CharField(blank=True, max_length=500, verbose_name='Spouse Name')),
                ('spouse_email', models.EmailField(blank=True, max_length=500, verbose_name='Spouse Email')),
                ('spouse_phone', models.CharField(max_length=12, verbose_name='Spouse Phone')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Designation', verbose_name='Designation')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Gender', verbose_name='Gender')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Language', verbose_name='Home Language')),
                ('marital_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Marital_Status', verbose_name='Marital Status')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('religion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Religion', verbose_name='Religion')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Title', verbose_name='Title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee Profile',
                'verbose_name_plural': 'Employee Profile',
                'ordering': ('employee_number',),
            },
        ),
    ]
