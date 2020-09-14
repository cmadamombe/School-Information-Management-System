from django.contrib.auth import views as auth_views
from simspro.students import views
from django.urls import include, path

app_name = "students"

urlpatterns = [
    path('students/', views.AddStudentView.as_view(), name='add_student'),
    path('student/update/', views.StudentUpdateView.as_view(), name='student_update'),
]