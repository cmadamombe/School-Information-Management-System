from django.contrib import admin
from simspro.students.models import Students

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Students Personal Details:', {  # The first fieldset is named “Employee personal details”
            'description': "Please capture the students personal details: ",  # The first option sets the description for the group
            #'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': (("user","title"), ("date_of_birth"), ("student_phone"), ("designation", "date_of_joining", "gender"), ("religion", "language", "nationality"), ("marital_status", "profile_image", "qualification"))
        }),

        ('Physical Address & Profile Summary:', {  # The second fieldset/group
            'description': "Please capture the student address and profile: ",  # The  option sets the description for the group
            'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': ("address", "student_profile_summary")
        }),

        ('Spouse Details:', {  # The first fieldset is named “Required Information”
            'description': "Please capture the spouse details: ",  # The first option sets the description for the group
            'classes': ('collapse',), #Adds the collapse class to the fieldset. This will apply a JavaScipt accordion style that will make the fieldset appear collapsed when the form first displays
            'fields': ("spouse_name", "spouse_email", "spouse_phone")
        }),
    )  
    # Chooses the fields to display on the form
    list_display = ["user", "s_id", "student_phone", "gender", "created_by", "created_date", "modified_by", "modified_date"]
    #The fields that will be used to search the database
    search_fields = ["user","s_id","student_email"]
    #Field the database according to the selected fields by default
    list_filter = ('gender', 'designation')
    #The results are in ascending order. To display results in descending order, use (-field_name e.g -user)
    ordering = ('s_id',)
