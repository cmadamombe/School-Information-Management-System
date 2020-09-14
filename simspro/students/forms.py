from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from simspro.students.models import Students
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError
from django.forms import ModelForm
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

class AddStudentForm(UserCreationForm):#As the base we used the built-in UserCreationForm, which defines the username and password fields. We extend this to include username, email and password.
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # Here we add the extra form fields that we will use to create another model object when the new user is created (Student model)
    student_phone = forms.CharField(required=False)
    gender  = forms.ModelChoiceField(queryset=Gender.objects.filter(is_active='True'), required=False) #filter by active status of the gender
    
    class Meta(UserCreationForm.Meta): 
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        #remove the help texts on the username field
        help_texts = {
            'username': None,
            
        }
    #avoid duplicate emails
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError('Another user with that email already exists')
        return email

    '''
    Note that the save method is decorated with the transaction.atomic, 
    to make sure those three operations are done in a single database transaction and avoid data 
    inconsistencies in case of error.
    '''
    @transaction.atomic
    def save(self, commit=True):
        # Pop the fields out of self.cleaned_data
        student_phone = self.cleaned_data.pop('student_phone', None)
        gender = self.cleaned_data.pop('gender', None)
        user = super(AddStudentForm, self).save(commit=False) #commit = false so not to save before checking user roles and is_active.
        #Inside the save method, I’m setting the is_true = true, so that the created user is given Student role by defaut.
        user.is_student = True
        user.is_active = True #is_active will make the user to be active and able to login the system
        user.save() #save user in the database
        #We create an Student profile to store the extra information, that is not available in the default user model.
        #now that we have successfully saved the user we can now use the user object just created to create a ParentProfile object with the extra form fields captured by the form
        Students.objects.create(user=user, student_phone=student_phone, gender=gender)
        return user

class StudentUpdateForm(ModelForm): #UserUpdateForm class inherits from ModelForm.
        title = forms.ModelChoiceField(queryset=Title.objects.filter(is_active='True'), required=True)
        student_number = forms.CharField(required=False, disabled=True)
        student_phone = forms.CharField(required=False, disabled=False)
        designation = forms.ModelChoiceField(queryset=Designation.objects.filter(is_active='True'), required=False)
        gender  = forms.ModelChoiceField(queryset=Gender.objects.filter(is_active='True'), required=False) #filter by active status of the gender
        date_of_birth = forms.DateField(disabled=True, required=False)
        religion = forms.ModelChoiceField(queryset=Religion.objects.filter(is_active='True'), required=False)
        language = forms.ModelChoiceField(queryset=Language.objects.filter(is_active='True'), required=False)
        nationality = forms.ModelChoiceField(queryset=Nationality.objects.filter(is_active='True'), required=False, disabled=False)
        qualification = forms.ModelChoiceField(queryset=Qualification.objects.filter(is_active='True'), required=False, disabled=True)
        address = forms.CharField(required=True, disabled=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 6}))
        student_profile_summary = forms.CharField(required=True, disabled=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 6}))
        marital_status = forms.ModelChoiceField(queryset=Marital_Status.objects.filter(is_active='True'), required=False, disabled=True)
        spouse_name = forms.CharField(required=False, disabled=False)
        spouse_email = forms.EmailField(required=False, disabled=False)
        spouse_phone = forms.CharField(required=False, disabled=False) 

        class Meta: #The ModelForm class has an internal Meta class which we use to pass in the metadata options the ModelForm class needs to render our form:
            model = Students
            fields = ['title', 'student_number', 'student_phone', 'designation', 'gender', 'date_of_birth', 'religion', 'language', 'nationality',
            'qualification', 'address', 'student_profile_summary', 'marital_status', 'spouse_name', 'spouse_email', 'spouse_phone']

            help_texts = {
            'username': None,
             }