#from django.contrib.auth.models import User
from django.db import models
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

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = 'Genders'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Designation(models.Model):
    description = models.CharField(verbose_name='Designation', max_length=500)

    class Meta:
        verbose_name = "Designation"
        verbose_name_plural = 'Designations'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Qualification(models.Model):
    description = models.CharField(verbose_name='Qualification', max_length=500)

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = 'Qualifications'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Nationality(models.Model):
    description = models.CharField(verbose_name='Nationality', max_length=500)

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = 'Nationalities'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Religion(models.Model):
    description = models.CharField(verbose_name='Religion', max_length=500)

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = 'Religions'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Language(models.Model):
    description = models.CharField(verbose_name='Home Language', max_length=500)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = 'Languages'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Marital_Status(models.Model):
    description = models.CharField(verbose_name='Marital Status', max_length=500)

    class Meta:
        verbose_name = "Marital Status"
        verbose_name_plural = 'Marital Status'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)

class Title(models.Model):
    description = models.CharField(verbose_name='Title', max_length=500)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = 'Titles'
        ordering = ('description',)

    def __str__(self):
        return "{}".format(self.description)