from django.urls import path
from . import views
from .views import (
    my_home_page_view,
)

app_name = "profiles"

urlpatterns = [
    path("", views.index),
    path("my-home-page", my_home_page_view, name="my-home-page-view"),
]