from django.contrib.auth import views as auth_views
from simspro.setup import views
from django.urls import include, path

app_name = "setup"

urlpatterns = [
    path('setup/', views.AddFeesView.as_view(), name='add_fees'),
]