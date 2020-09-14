from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
from simspro.setup.models import ( 
     Gender, 
     Designation, 
     Qualification, 
     Nationality, 
     Religion, 
     Language, 
     Marital_Status, 
     Title
)
#Import function to calculate unique IDs
from django.db.models import Max
from simspro.utils.employees.utils import (
    fill_with_zeros, 
    increment_id
)
# Create your models here.
class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Title')    
    #employee_number = models.CharField(max_length=5000, blank=False, null=False, unique=True, verbose_name='Employee Number')
    #The employee number is created automatically by the function from the utils
    e_id = models.CharField(blank=True, primary_key=False, unique=True, editable=False, max_length=1024, verbose_name='Employee ID')
    employee_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Employee Phone')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Designation')
    date_of_joining = models.DateField(blank=True, null=True, verbose_name='Date Joined')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Religion')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Home Language')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Nationality')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Highest Qualification')
    address = models.TextField(blank=True, null=True, verbose_name='Physical Address')
    teacher_profile_summary = models.TextField(blank=True, null=True, verbose_name='Employee Profile Summary')
    marital_status = models.ForeignKey(Marital_Status, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Marital Status')
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Profile Image')
    spouse_name = models.CharField(blank=True, null=True, max_length=500, verbose_name='Spouse Name')
    spouse_email = models.EmailField(blank=True, null=True, max_length=500, verbose_name='Spouse Email')
    spouse_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Spouse Phone')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')

    class Meta:
        """Meta definition for Employee."""
        verbose_name = "Employee Profile"
        verbose_name_plural = 'Employees Profile'
        ordering = ('e_id',)

    #We override the default save method in the 'std' class so that we can use our own.
    def save(self, *args, **kwargs):
        if not self.e_id:
            id_here = Employees.objects.aggregate(x=Max('e_id'))["x"]
            if id_here:
                self.e_id = increment_id(id_here)
            else:
                self.e_id = "EM100300"
        super(Employees, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.user)
