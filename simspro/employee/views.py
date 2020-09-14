from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from simspro.employee.forms import AddEmployeeForm, EmployeeUpdateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
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
        #form.instance.created_by.set([self.request.user])
        messages.add_message(self.request, messages.SUCCESS, ("New employee details have been successfully added!"))
        return super().form_valid(form)

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    form_class = EmployeeUpdateForm
    template_name = 'employee/employee_update_form.html'
    success_url = reverse_lazy('employee_update')

    def get_success_url(self):
        return reverse("employee:employee_update")#, kwargs={"username": self.request.user.username})

    def get_object(self):
        return Employees.objects.get(user=self.request.user)
       
    def form_valid(self, form):
        #form.instance.modified_by.set([self.request.user])
        messages.add_message(
            self.request, messages.INFO, _("The employee information have been successfully updated")
        )
        return super().form_valid(form)