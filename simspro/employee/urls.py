from django.contrib.auth import views as auth_views
from simspro.employee import views
from django.urls import include, path

app_name = "employee"

urlpatterns = [
    path('employee/add/new', views.AddEmployeeView.as_view(), name='add_employee'),
    path('employee/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
]