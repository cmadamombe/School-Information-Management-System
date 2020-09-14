from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import UpdateView
User = get_user_model()
from django.urls import reverse
from django.urls import reverse_lazy
from simspro.users.forms import UserUpdateForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update_form.html'
    success_url = reverse_lazy('user_update')

    def get_success_url(self):
        return reverse("users:user_update") #kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        #form.instance.modified_by.set([self.request.user])
        messages.add_message(
            self.request, messages.INFO, _("The personal information have NOT been updated.  To update your personal details, please contact your administrator.")
        )
        return super().form_valid(form)




