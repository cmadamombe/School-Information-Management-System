'''
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from simspro.setup.models import SchoolProfile

class SchoolProfileDetailView(LoginRequiredMixin, DetailView):

    model = SchoolProfile
    slug_field = "name"
    slug_url_kwarg = "name"

school_profile_detail_view = SchoolProfileDetailView.as_view()

class SchoolProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = SchoolProfile
    fields = '__all__'

    def get_success_url(self):
        return reverse("setup:detail", kwargs={"name": self.request.user.username})

    def get_object(self):
        #return SchoolProfile.objects.get(name=self.request.user.username)
        return SchoolProfile.objects.get()

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("School details successfully updated")
        )
        return super().form_valid(form)


school_profile_update_view = SchoolProfileUpdateView.as_view()


class SchoolProfileRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("setup:detail", kwargs={"username": self.request.user.username})

school_profile_redirect_view = SchoolProfileRedirectView.as_view()

'''
