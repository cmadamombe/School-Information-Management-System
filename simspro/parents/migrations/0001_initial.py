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
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(blank=True, editable=False, max_length=1024, unique=True, verbose_name='Parent ID')),
                ('parent_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Parent Phone')),
                ('date_of_joining', models.DateField(blank=True, null=True, verbose_name='Date Joined')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Physical Address')),
                ('parent_profile_summary', models.TextField(blank=True, null=True, verbose_name='Parent Profile Summary')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Profile Image')),
                ('spouse_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Spouse Name')),
                ('spouse_email', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Spouse Email')),
                ('spouse_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Spouse Phone')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Date Modified')),
                ('par_initials', models.CharField(blank=True, max_length=12, null=True, verbose_name='Parent Initials')),
                ('par_id', models.CharField(blank=True, max_length=500, null=True, verbose_name='Parent ID')),
                ('par_home_telephone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Parent Home Phone')),
                ('par_fax', models.CharField(blank=True, max_length=12, null=True, verbose_name='Parent Fax')),
                ('par_postal_box', models.TextField(blank=True, null=True, verbose_name='Parent Postal Address')),
                ('par_employer', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Employer Name')),
                ('par_work_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Work Phone')),
                ('par_work_email', models.EmailField(blank=True, max_length=500, null=True, verbose_name='Work Email')),
                ('par_work_addres', models.TextField(blank=True, null=True, verbose_name='Parent Work Address')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Designation', verbose_name='Designation')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Gender', verbose_name='Gender')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Language', verbose_name='Home Language')),
                ('marital_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Marital_Status', verbose_name='Marital Status')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Nationality', verbose_name='Nationality')),
                ('par_id_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.ID_Types', verbose_name='ID_Types')),
                ('par_occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Occupation', verbose_name='Occupation')),
                ('par_occupation_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Occupation_Status', verbose_name='Occupation Status')),
                ('par_preferred_communication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Communication_Methods', verbose_name='Preferred Communication Language')),
                ('qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Qualification', verbose_name='Highest Qualification')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Religion', verbose_name='Religion')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setup.Title', verbose_name='Title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parent Profile',
                'verbose_name_plural': 'Parents Profile',
                'ordering': ('p_id',),
            },
        ),
    ]
