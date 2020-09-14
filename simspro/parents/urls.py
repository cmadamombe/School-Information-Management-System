from django.contrib.auth import views as auth_views
from simspro.parents import views
from django.urls import include, path

app_name = "parents"

urlpatterns = [
    path('parents/', views.AddParentView.as_view(), name='add_parent'),
     path('parent/update/', views.ParentUpdateView.as_view(), name='parent_update'),
]