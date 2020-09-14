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
     Ethnics,
     Language_Preferences,
     Education_Types,
     Main_Relationships,
     Family_Status,
     Chronic_Diseases,
     Allergies,
     Provinces,
     Highest_Grade,
     Reasons_For_Leaving,
     Parent_Types,
     Communication_Methods,
     Occupation_Status,
     Occupation,
     GradeLevel,
     Classes,
     Parent_Deceased,
     Medical_Aid,
     Countries
)
from simspro.parents.models import Parents
#Import function to calculate unique IDs
from django.db.models import Max
from simspro.utils.students.utils import (
    fill_with_zeros, 
    increment_id
)

# Create your models here.
class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Title') 
    s_id = models.CharField(blank=True, unique=True, primary_key=False, editable=False, max_length=1024, verbose_name='Student ID')
    student_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Student Phone')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Designation')
    date_of_joining = models.DateField(blank=True, null=True, verbose_name='Date Joined')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Gender')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Religion')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Home Language')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Nationality')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Highest Qualification')
    address = models.TextField(blank=True, null=True, verbose_name='Physical Address')
    student_profile_summary = models.TextField(blank=True, null=True, verbose_name='Student Profile Summary')
    marital_status = models.ForeignKey(Marital_Status, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Marital Status')
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Profile Image')
    spouse_name = models.CharField(blank=True, null=True, max_length=500, verbose_name='Spouse Name')
    spouse_email = models.EmailField(blank=True, null=True, max_length=500, verbose_name='Spouse Email')
    spouse_phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Spouse Phone')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='student_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='student_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    #the followong fields have been added to the student model > 7/5/2020 by Chuck Madamombe
    stu_id_type = models.ForeignKey(ID_Types, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='ID Types')
    stu_id = models.CharField(max_length=500, blank=True, null=True, verbose_name='Student ID')
    stu_ethnic_group = models.ForeignKey(Ethnics, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Ethnics')
    stu_preferred_language = models.ForeignKey(Language_Preferences, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Language Preference')
    stu_admission_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Student Admission')
    stu_grade = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Student Grade')
    stu_class = models.ForeignKey(Classes, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Student Class')
    stu_pre_primary_education = models.ForeignKey(Education_Types, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Student Pre-Primary Education Type')
    stu_nxt_of_kin_firstname = models.CharField(max_length=500, blank=True, null=True, verbose_name='Next of Kin First Name')
    stu_nxt_of_kin_lastname = models.CharField(max_length=500, blank=True, null=True, verbose_name='Next of Kin Last Name')
    stu_nxt_of_kin_phone = models.CharField(max_length=500, blank=True, null=True, verbose_name='Next of Kin Phone')
    stu_nxt_of_kin_email = models.EmailField(blank=True, null=True, max_length=500, verbose_name='Next of Kin Email')
    stu_nxt_of_kin_work_address = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Next of Kin Work Address')
    stu_nxt_of_kin_home_address = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Next of Kin Home Address')
    stu_nxt_of_kin_relationship = models.ForeignKey(Main_Relationships, on_delete=models.CASCADE, blank=True, null=True, editable=True, related_name='next_of_kin_relationship', verbose_name='Relationships')
    stu_family_status = models.ForeignKey(Family_Status, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Family Status')
    stu_parents_deseased = models.ForeignKey(Parent_Deceased, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Parent deceased')
    stu_chronic_disease  = models.ForeignKey(Chronic_Diseases, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Chronic Diseases')
    stu_allergies = models.ForeignKey(Allergies, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Allergies')
    stu_on_medication = models.BooleanField(default=True, verbose_name='Student on Medication')
    stu_medical_aid_name = models.ForeignKey(Medical_Aid, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Medical Aid Name')
    stu_medical_aid_number = models.CharField(max_length=500, blank=True, null=True, verbose_name='Medical Aid Number')
    stu_medical_aid_phone = models.CharField(max_length=500, blank=True, null=True, verbose_name='Medical Aid Phone')
    stu_medical_aid_is_primary_member = models.BooleanField(default=True, verbose_name='Primary Member')
    stu_previous_school_name = models.CharField(max_length=500, blank=True, null=True, verbose_name='Previous School Name')
    stu_previous_school_phone = models.CharField(max_length=500, blank=True, null=True, verbose_name='Previous School Phone')
    stu_previous_school_email = models.EmailField(blank=True, null=True, max_length=500, verbose_name='Previous School Email')
    stu_previous_school_address = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Previous School Address')
    stu_previous_school_country = models.ForeignKey(Countries, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Previous School Country')
    stu_previous_school_province = models.ForeignKey(Provinces, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Previous School Province')
    stu_previous_school_highest_grade = models.ForeignKey(Highest_Grade, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Previous School Highest Grade')
    stu_previous_school_reason_for_leaving = models.ForeignKey(Reasons_For_Leaving, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Previous School Reason for Leaving')
    stu_main_parent_guardian_type = models.ForeignKey(Parent_Types, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Parent Type')
    stu_main_parent_guardian = models.ForeignKey(Parents, on_delete=models.CASCADE, blank=True, null=True, editable=True, related_name='main_parent', verbose_name='Main Parent/Guardian')
    stu_main_parent_guardian_relationship = models.ForeignKey(Main_Relationships, on_delete=models.CASCADE, blank=True, null=True, editable=True, related_name='parent_relationship', verbose_name='Relationship to Student')
    stu_is_leaving_with_this_parent = models.BooleanField(default=True, verbose_name='Student Leaves with Parent')
    parent_is_accountable = models.BooleanField(default=True, verbose_name='Parent is Accountable')
    stu_preferred_communication = models.ForeignKey(Communication_Methods, on_delete=models.CASCADE, blank=True, null=True, editable=True, verbose_name='Preferred Communication Method')

    class Meta:
        """Meta definition for Student."""
        verbose_name = "Student Profile"
        verbose_name_plural = 'Student Profiles'
        ordering = ('s_id',)

    #We override the default save method in the 'std' class so that we can use our own.
    def save(self, *args, **kwargs):
        if not self.s_id:
            id_here = Students.objects.aggregate(x=Max('s_id'))["x"]
            if id_here:
                self.s_id = increment_id(id_here)
            else:
                self.s_id = "ST400200"
        super(Students, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.user)

