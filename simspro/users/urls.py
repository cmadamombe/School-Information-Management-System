from django.contrib.auth import views as auth_views
from simspro.users import views
from django.urls import include, path

app_name = "users"
urlpatterns = [
    path('user/update/', views.UserUpdateView.as_view(), name='user_update'),
]
