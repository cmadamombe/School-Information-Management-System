from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Fees
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django import forms

class AddFeesView(LoginRequiredMixin, CreateView):
    model = Fees
    template_name = 'setup/add_fees.html'
    fields = ('fee_code', 'fee_description', 'fee_amount', 'academic_year', 'term', 'grade_level')
    success_url = reverse_lazy('add_fees')

    def get_success_url(self):
        return reverse("setup:add_fees")
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ("The Fee Instance Has Been Successfully Created."))
        return super().form_valid(form)