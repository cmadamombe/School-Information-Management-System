from django.contrib import admin
#from django.contrib.auth import admin as auth_admin
#from .models import SchoolProfile
#from django.contrib.auth import get_user_model
#from simspro.users.forms import UserChangeForm, UserCreationForm
from simspro.setup.models import Gender, Designation, Qualification, Nationality, Religion, Language, Marital_Status, Title
'''
# Register your models here.

@admin.register(SchoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
    fieldsets = (("School Details", {"fields": ("name","email", "address", "school_start_time", "school_end_time")}),)
    list_display = ["name", "email", "address", "school_start_time", "school_end_time", "created_by", "created_date", "modified_by", "modified_date"]
    #search_fields = ["name","username","email"]
'''
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    fieldsets = (("Gender Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    fieldsets = (("Designation Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    fieldsets = (("Qualification Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Nationality)
class QualificationAdmin(admin.ModelAdmin):
    fieldsets = (("Nationality Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    fieldsets = (("Nationality Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    fieldsets = (("Language Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Marital_Status)
class Marital_StatusAdmin(admin.ModelAdmin):
    fieldsets = (("Marital Status Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    fieldsets = (("Title Details", {"fields": ("description",)}),)
    list_display = ["description"]
    #search_fields = ["name","username","email"]