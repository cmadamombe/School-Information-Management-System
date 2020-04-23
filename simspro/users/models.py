from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=1000)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
