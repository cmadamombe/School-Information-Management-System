from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from simspro.parents.forms import AddParentForm, ParentUpdateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Parents

# Create your views here.

class AddParentView(CreateView, LoginRequiredMixin):
    model = User
    form_class = AddParentForm
    template_name = 'parents/add_parent.html'
    #success_url = reverse_lazy('account_login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'parent'
        return super().get_context_data(**kwargs)
    
    #def get_success_url(self):
        #return reverse("users:account_login")

    def form_valid(self, form):
        user = form.save(form)
        #form.instance.created_by.set([self.request.user]) 
        login(self.request, user)#Redirect to login after the form is successfully submitted!
        messages.add_message(self.request, messages.SUCCESS, ("Your New Account Has Been Successfully Created. You Can Now login."))
        return super().form_valid(form)

class ParentUpdateView(LoginRequiredMixin, UpdateView):
    model = Parents
    form_class = ParentUpdateForm
    template_name = 'parents/parent_update_form.html'
    success_url = reverse_lazy('parent_update')

    def get_success_url(self):
        return reverse("parent:parent_update")#, kwargs={"username": self.request.user.username})

    def get_object(self):
        return Parents.objects.get(user=self.request.user)
       
    def form_valid(self, form):
        #form.instance.modified_by.set([self.request.user])
        messages.add_message(self.request, messages.INFO, ("The parent information have been successfully updated"))
        return super().form_valid(form)
        
