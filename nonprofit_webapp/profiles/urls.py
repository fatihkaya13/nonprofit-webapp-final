from django.urls import path
from . import views
from .views import (
    my_home_page_view,
    my_applied_jobs_view,
    my_donations_view,
)

app_name = "profiles"

urlpatterns = [
    path("", views.index),
    path("my-home-page", my_home_page_view, name="my-home-page-view"),
    path("my-applied-jobs", my_applied_jobs_view, name="my-applied-jobs"),
    path("my-donations", views.my_donations_view, name="my-donations")
]