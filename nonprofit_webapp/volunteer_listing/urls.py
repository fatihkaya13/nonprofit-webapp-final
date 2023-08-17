from django.urls import path
from . import views

app_name = "volunteer_listing"

urlpatterns = [
    path("", views.jobs_list_view, name="jobs_list_view")
]