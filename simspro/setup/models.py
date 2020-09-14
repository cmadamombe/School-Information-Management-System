#from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
'''
# Create your models here.
class SchoolProfile(models.Model):
    name = models.CharField(verbose_name='School Name', max_length=500)
    email = models.EmailField(verbose_name='School Email', max_length=254)
    address = models.TextField(verbose_name='School Address', blank=True, null=True)
    school_start_time = models.TimeField(verbose_name='School Start Time', auto_now=False, auto_now_add=False)
    school_end_time = models.TimeField(verbose_name='School End Time', auto_now=False, auto_now_add=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, verbose_name='Created By')
    created_date = models.DateTimeField(verbose_name='Date Created', auto_now_add=True, editable=False)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, verbose_name='Modified By')
    modified_date = models.DateTimeField(('Last Modified'), auto_now=True, editable=False)

    class Meta:
        verbose_name = "School Profile"
        ordering = ('name',)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)
'''
class Gender(models.Model):
    description = models.CharField(verbose_name='Gender', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = 'Genders'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Designation(models.Model):
    description = models.CharField(verbose_name='Designation', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Designation"
        verbose_name_plural = 'Designations'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Qualification(models.Model):
    description = models.CharField(verbose_name='Qualification', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = 'Qualifications'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Nationality(models.Model):
    description = models.CharField(verbose_name='Nationality', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = 'Nationalities'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Religion(models.Model):
    description = models.CharField(verbose_name='Religion', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = 'Religions'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Language(models.Model):
    description = models.CharField(verbose_name='Home Language', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = 'Languages'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Marital_Status(models.Model):
    description = models.CharField(verbose_name='Marital Status', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Marital Status"
        verbose_name_plural = 'Marital Status'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Title(models.Model):
    description = models.CharField(verbose_name='Title', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = 'Titles'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class AcademicYear(models.Model):
    academic_year = models.IntegerField(verbose_name='Academic Year')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Academic Year"
        verbose_name_plural = 'Academic Years'
        ordering = ('academic_year',)

    def __str__(self):
        return "{}".format(self.academic_year)

class Term(models.Model):
    term = models.IntegerField(verbose_name='Term')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Term"
        verbose_name_plural = 'Terms'
        ordering = ('term',)

    def __str__(self):
        return "{}".format(self.term)

class GradeLevel(models.Model):
    grade_code = models.CharField(verbose_name='Grade Code', max_length=5)
    grade_level = models.CharField(verbose_name='Grade Level', max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Grade Level"
        verbose_name_plural = 'Grade Levels'
        ordering = ('grade_code',)

    def __str__(self):
        return "{}".format(self.grade_code)

class Fees(models.Model):
    fee_code = models.CharField(verbose_name='Fee Code', max_length=50)
    fee_description = models.CharField(verbose_name='Fees Description', max_length=500)
    fee_amount = models.FloatField(verbose_name='Fees Amount')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name='Academic Year')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='Term')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, verbose_name='Grade Level')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='fee_created_by', verbose_name='Created By')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date Created')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, editable=False, related_name='fee_modified_by', verbose_name='Modified By')
    modified_date = models.DateTimeField(auto_now=True, editable=False, verbose_name='Date Modified')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "School Fees"
        verbose_name_plural = 'School Fees'
        ordering = ('fee_code',)

    def __str__(self):
        return "{}".format(self.fee_code)

#The following models were added by Chuck Madamombe on 10 May 2020
class ID_Types(models.Model):
    description = models.CharField(verbose_name='ID Types', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "ID Type"
        verbose_name_plural = 'ID Types'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Ethnics(models.Model):
    description = models.CharField(verbose_name='Ethnics', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Ethnic"
        verbose_name_plural = 'Ethnics'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Language_Preferences(models.Model):
    description = models.CharField(verbose_name='Language Preference', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Language Preference"
        verbose_name_plural = 'Language Preferences'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Education_Types(models.Model):
    description = models.CharField(verbose_name='Education Type', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Education Type"
        verbose_name_plural = 'Education Types'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Main_Relationships(models.Model):
    description = models.CharField(verbose_name='Relationships', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Relationship"
        verbose_name_plural = 'Relationships'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Family_Status(models.Model):
    description = models.CharField(verbose_name='Family Status', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Family Status"
        verbose_name_plural = 'Family Status'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Chronic_Diseases(models.Model):
    description = models.CharField(verbose_name='Chronic Diseases', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Chronic Disease"
        verbose_name_plural = 'Chronic Diseases'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Allergies(models.Model):
    description = models.CharField(verbose_name='Allergies', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Allergies"
        verbose_name_plural = 'Allergies'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Provinces(models.Model):
    description = models.CharField(verbose_name='Provinces', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = 'Provinces'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Highest_Grade(models.Model):
    description = models.CharField(verbose_name='Highest Grade', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Highest Grade"
        verbose_name_plural = 'Highest Grades'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Reasons_For_Leaving(models.Model):
    description = models.CharField(verbose_name='Reason For Leaving', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Reason For Leaving"
        verbose_name_plural = 'Reasons For Leaving'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Parent_Types(models.Model):
    description = models.CharField(verbose_name='Parent Types', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Parent Type"
        verbose_name_plural = 'Parent Types'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Communication_Methods(models.Model):
    description = models.CharField(verbose_name='Preferred Communication Method', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Preferred Communication Method"
        verbose_name_plural = 'Preferred Communication Methods'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Occupation_Status(models.Model):
    description = models.CharField(verbose_name='Occupation Status', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Occupation Status"
        verbose_name_plural = 'Occupation Status'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Occupation(models.Model):
    description = models.CharField(verbose_name='Occupation', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = 'Occupation'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Classes(models.Model):
    class_code = models.CharField(verbose_name='Class Code', max_length=500)
    description = models.CharField(verbose_name='Class Description', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Class Description"
        verbose_name_plural = 'Classes Description'
        ordering = ('class_code',)

    def __str__(self):
        return "{}".format(self.class_code)

class Parent_Deceased(models.Model):
    description = models.CharField(verbose_name='Parent Deceased', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Parent Deceased"
        verbose_name_plural = 'Parents Deceased'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Medical_Aid(models.Model):
    description = models.CharField(verbose_name='Medical Aid Name', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Medical Aid"
        verbose_name_plural = 'Medical Aid'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Countries(models.Model):
    description = models.CharField(verbose_name='Countries', max_length=500)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = 'Countries'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)
