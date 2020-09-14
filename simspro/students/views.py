from django.contrib import messages
#from django.shortcuts import render
#from django.contrib.auth import login
#from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from simspro.students.forms import AddStudentForm, StudentUpdateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.urls import reverse_lazy
from simspro.students.models import Students

# Create your views here.

class AddStudentView(LoginRequiredMixin, CreateView):
    model = User
    form_class = AddStudentForm
    template_name = 'students/add_student.html'
    success_url = reverse_lazy('add_student')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse("students:add_student")

    def form_valid(self, form):
        #form.instance.created_by.set([self.request.user]) 
        messages.add_message(self.request, messages.SUCCESS, ("The Student Details Have Been Successfully Added."))
        return super().form_valid(form)

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentUpdateForm
    template_name = 'students/student_update_form.html'
    success_url = reverse_lazy('student_update')

    def get_success_url(self):
        return reverse("students:student_update")#, kwargs={"username": self.request.user.username})

    def get_object(self):
        return Students.objects.get(user=self.request.user)
       
    def form_valid(self, form):
        #form.instance.modified_by.set([self.request.user])
        messages.add_message(
            self.request, messages.INFO, _("The student information have been successfully updated")
        )
        return super().form_valid(form)
        
