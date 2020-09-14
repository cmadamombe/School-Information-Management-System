from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from simspro.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User Details", {"fields": ("is_admin", "is_teacher", "is_student", "is_parent", "is_secretary", "middle_name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "first_name", "middle_name", "last_name", "email", "is_admin", "is_teacher", "is_student", "is_parent", "is_secretary", "is_staff", "is_superuser", "is_active"]
    search_fields = ["first_name","username","email"]
    ordering = ('first_name',)


