# Generated by Django 3.0.5 on 2020-05-11 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setup', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.CharField(blank=True, editable=False, max_length=1024, unique=True, verbose_name='Employee ID')),
                ('employee_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Employee Phone')),
                ('date_of_joining', models.DateField(blank=True, null=True, verbose_name='Date Joined')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Physical Address')),
                ('teacher_profile_summary', models.TextField(blank=True, null=True, verbose_name='Employee Profile Summary')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Profile Image')),
                ('spouse_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Spouse Name')),
                ('spouse_email', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Spouse Email')),
                ('spouse_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Spouse Phone')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Designation', verbose_name='Designation')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Gender', verbose_name='Gender')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Language', verbose_name='Home Language')),
                ('marital_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Marital_Status', verbose_name='Marital Status')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Nationality', verbose_name='Nationality')),
                ('qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Qualification', verbose_name='Highest Qualification')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Religion', verbose_name='Religion')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Title', verbose_name='Title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee Profile',
                'verbose_name_plural': 'Employees Profile',
                'ordering': ('e_id',),
            },
        ),
    ]
