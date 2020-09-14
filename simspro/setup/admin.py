from django.contrib import admin
#from django.contrib.auth import admin as auth_admin
#from .models import SchoolProfile
#from django.contrib.auth import get_user_model
#from simspro.users.forms import UserChangeForm, UserCreationForm
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
     Countries,
     AcademicYear,
     Fees,
     Term
)
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
    fieldsets = (("Gender Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    fieldsets = (("Designation Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    fieldsets = (("Qualification Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Nationality)
class QualificationAdmin(admin.ModelAdmin):
    fieldsets = (("Nationality Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    fieldsets = (("Nationality Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    fieldsets = (("Language Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Marital_Status)
class Marital_StatusAdmin(admin.ModelAdmin):
    fieldsets = (("Marital Status Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    fieldsets = (("Title Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    fieldsets = (("Academic Details", {"fields": ("academic_year", "is_active",)}),)
    list_display = ["academic_year", "is_active"]
    #search_fields = ["name","username","email"]

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    fieldsets = (("Term Details", {"fields": ("term", "is_active",)}),)
    list_display = ["term", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('term',)

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    fieldsets = (("Grade Level Details", {"fields": ("grade_code", "grade_level", "is_active",)}),)
    list_display = ["grade_code", "grade_level", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('grade_code',)

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Fees Details:', {  # The first fieldset is named “Employee personal details”
            'description': "Please capture the fees details: ",  # The first option sets the description for the group
            #'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': ("fee_code","fee_description", "fee_amount", "academic_year", "term", "grade_level", "is_active")
        }),
    )  
    # Chooses the fields to display on the form
    list_display = ["fee_code", "fee_description", "fee_amount", "academic_year", "term", "grade_level", "created_by", "created_date", "modified_by", "modified_date", "is_active"]
    #The fields that will be used to search the database
    search_fields = ["fee_code","fee_description"]
    #Field the database according to the selected fields by default
    list_filter = ('grade_level', 'academic_year')
    #The results are in ascending order. To display results in descending order, use (-field_name e.g -user)
    ordering = ('fee_code',)

@admin.register(ID_Types)
class ID_TypesAdmin(admin.ModelAdmin):
    fieldsets = (("ID Types Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Ethnics)
class EthnicsAdmin(admin.ModelAdmin):
    fieldsets = (("Ethnics Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Language_Preferences)
class Language_PreferencesAdmin(admin.ModelAdmin):
    fieldsets = (("Language Preferences Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Education_Types)
class Education_TypesAdmin(admin.ModelAdmin):
    fieldsets = (("Education Types Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Main_Relationships)
class Main_RelationshipsAdmin(admin.ModelAdmin):
    fieldsets = (("Main_Relationships Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Family_Status)
class Family_StatusAdmin(admin.ModelAdmin):
    fieldsets = (("Family Status Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Chronic_Diseases)
class Chronic_DiseasesAdmin(admin.ModelAdmin):
    fieldsets = (("Chronic Diseases Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Allergies)
class AllergiesAdmin(admin.ModelAdmin):
    fieldsets = (("Allergies Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Provinces)
class ProvincesAdmin(admin.ModelAdmin):
    fieldsets = (("Provinces Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Highest_Grade)
class Highest_GradeAdmin(admin.ModelAdmin):
    fieldsets = (("Highest Grade Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Reasons_For_Leaving)
class Reasons_For_LeavingAdmin(admin.ModelAdmin):
    fieldsets = (("Reasons For Leaving Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Parent_Types)
class Parent_TypesAdmin(admin.ModelAdmin):
    fieldsets = (("Parent Types Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Communication_Methods)
class Communication_MethodsAdmin(admin.ModelAdmin):
    fieldsets = (("Communication Methods Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Occupation_Status)
class Occupation_StatusAdmin(admin.ModelAdmin):
    fieldsets = (("Occupation Status Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    fieldsets = (("Occupation Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    fieldsets = (("Classes Details", {"fields": ("class_code", "description", "is_active",)}),)
    list_display = ["class_code", "description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('class_code',)

@admin.register(Parent_Deceased)
class Parent_DeceasedAdmin(admin.ModelAdmin):
    fieldsets = (("Parent Deceased Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Medical_Aid)
class Medical_AidAdmin(admin.ModelAdmin):
    fieldsets = (("Medical Aid Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)

@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    fieldsets = (("Countries Details", {"fields": ("description", "is_active",)}),)
    list_display = ["description", "is_active"]
    #search_fields = ["name","username","email"]
    ordering = ('description',)