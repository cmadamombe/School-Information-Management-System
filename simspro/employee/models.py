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
#Function to calculate random student numbers
from simspro.utils.utils import create_employee_number

# Create your models here.
class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Title') 
    first_name = models.CharField(max_length=300, blank=False, null=False, verbose_name='First Name')
    other_name = models.CharField(max_length=300, blank=False, null=False,verbose_name='Middle Name')
    last_name  = models.CharField(max_length=300, blank=False, null=False, verbose_name='Last Name')   
    #employee_number = models.CharField(max_length=5000, blank=False, null=False, unique=True, verbose_name='Employee Number')
    #The employee number is created automatically by the function from the utils
    employee_number = models.IntegerField(
        blank=True,
        editable=False,
        unique=True,
        default=create_employee_number(),
        verbose_name='Employee Number'
      )
    employee_email = models.EmailField(blank=True, max_length=500, verbose_name='Employee Email')
    employee_phone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Employee Phone')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True, verbose_name='Designation')
    date_of_joining = models.DateField(verbose_name='Date Joined')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Gender')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Religion')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Home Language')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Nationality')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Highest Qualification')
    address = models.TextField(blank=True, null=True, verbose_name='Physical Address')
    teacher_profile_summary = models.TextField(blank=True, null=True, verbose_name='Employee Profile Summary')
    marital_status = models.ForeignKey(Marital_Status, on_delete=models.CASCADE, null=True, editable=True, verbose_name='Marital Status')
    profile_image = models.ImageField(upload_to='images/', blank=True, verbose_name='Profile Image')
    spouse_name = models.CharField(blank=True, max_length=500, verbose_name='Spouse Name')
    spouse_email = models.EmailField(blank=True, max_length=500, verbose_name='Spouse Email')
    spouse_phone = models.CharField(max_length=12, blank=False, null=False, verbose_name='Spouse Phone')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, related_name='created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, related_name='modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')

    class Meta:
        """Meta definition for Employee."""
        verbose_name = "Employee Profile"
        verbose_name_plural = 'Employee Profile'
        ordering = ('employee_number',)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.other_name, self.last_name)
