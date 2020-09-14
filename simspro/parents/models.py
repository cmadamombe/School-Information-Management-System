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
     Title,
     ID_Types,
     Language_Preferences,
     Communication_Methods,
     Occupation_Status,
     Occupation
)
#Import function to calculate unique IDs
from django.db.models import Max
from simspro.utils.parents.utils import (
    fill_with_zeros, 
    increment_id
)

# Create your models here.
class Parents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Title') 
    #employee_number = models.CharField(max_length=5000, blank=False, null=False, unique=True, verbose_name='Employee Number')
    #The parent ID number is created automatically by the function from the utils
    p_id = models.CharField(blank=True, primary_key=False, unique=True, editable=False, max_length=1024, verbose_name='Parent ID')
    parent_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Parent Phone')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Designation')
    date_of_joining = models.DateField(blank=True, null=True, verbose_name='Date Joined')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Religion')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Home Language')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Nationality')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Highest Qualification')
    address = models.TextField(blank=True, null=True, verbose_name='Physical Address')
    parent_profile_summary = models.TextField(blank=True, null=True, verbose_name='Parent Profile Summary')
    marital_status = models.ForeignKey(Marital_Status, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Marital Status')
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Profile Image')
    spouse_name = models.CharField(blank=True, null=True, max_length=500, verbose_name='Spouse Name')
    spouse_email = models.EmailField(blank=True, null=True, max_length=500, verbose_name='Spouse Email')
    spouse_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Spouse Phone')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='parent_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='parent_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    #the followong fields have been added to the student model > 7/5/2020 by Chuck Madamombe
    par_initials = models.CharField(max_length=12, blank=True, null=True, verbose_name='Parent Initials')
    par_id_type = models.ForeignKey(ID_Types, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='ID_Types')
    par_id = models.CharField(max_length=500, blank=True, null=True, verbose_name='Parent ID')
    par_preferred_communication = models.ForeignKey(Communication_Methods, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Preferred Communication Language')
    par_home_telephone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Parent Home Phone')
    par_fax = models.CharField(max_length=12, blank=True, null=True, verbose_name='Parent Fax')
    par_postal_box = models.TextField(blank=True, null=True, verbose_name='Parent Postal Address')
    par_occupation_status = models.ForeignKey(Occupation_Status, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Occupation Status')
    par_occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Occupation')
    par_employer = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Employer Name')
    par_work_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Work Phone')
    par_work_email = models.EmailField(max_length=500, blank=True, null=True, verbose_name='Work Email')
    par_work_addres = models.TextField(blank=True, null=True, verbose_name='Parent Work Address')
    
    class Meta:
        """Meta definition for Parent."""
        verbose_name = "Parent Profile"
        verbose_name_plural = 'Parents Profile'
        ordering = ('p_id',)
    
    '''We override the default save method in the 'std' class so that we can use our own.'''
    def save(self, *args, **kwargs):
        if not self.p_id:
            id_here = Parents.objects.aggregate(x=Max('p_id'))["x"]
            if id_here:
                self.p_id = increment_id(id_here)
            else:
                self.p_id = "PA100200"
        super(Parents, self).save(*args, **kwargs)
    
    def __str__(self):
        return '{}'.format(self.user)

