from django.urls import path
from . import views

app_name="donations"

urlpatterns = [
    path("", views.index),
    path('donate/', views.donation_form, name='donate'),
    path('donation_success/', views.donation_success, name='donation-success'),
]