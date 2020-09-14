from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    middle_name = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Middle Name')

    def get_absolute_url(self):
        return reverse("users:user_update", kwargs={"username": self.username})
