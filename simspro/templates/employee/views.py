from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from simspro.employee.forms import AddEmployeeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .models import Employees

# Create your views here.

class AddEmployeeView(LoginRequiredMixin, CreateView):
    model = User
    form_class = AddEmployeeForm
    template_name = 'employee/add_employee.html'
    success_url = reverse_lazy('add_employee')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse("employee:add_employee")

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, ("New employee details have been successfully added!"))
        return super().form_valid(form)

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employees
    slug_field = "username"
    slug_url_kwarg = "username"
employee_detail_view = EmployeeDetailView.as_view()

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    fields = ['title', 'employee_number', 'employee_phone', 'designation', 'gender', 'date_of_birth', 'religion', 'language', 'nationality',
    'qualification', 'address', 'teacher_profile_summary', 'marital_status', 'spouse_name', 'spouse_email', 'spouse_phone']

    def get_success_url(self):
        return reverse("employee:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return Employees.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("The employee information have been successfully updated")
        )
        return super().form_valid(form)

employee_update_view = EmployeeUpdateView.as_view()

class EmployeeRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("employee:detail", kwargs={"username": self.request.user.username})

employee_redirect_view = EmployeeRedirectView.as_view()

