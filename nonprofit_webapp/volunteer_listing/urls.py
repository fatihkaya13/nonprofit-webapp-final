from django.urls import path

from .views import (
    jobs_list_view,
    apply_job,
    withdraw_job_application
)

app_name = "volunteer_listing"

urlpatterns = [
    path("", jobs_list_view, name="jobs-list-view"),
    path("apply-job/", apply_job, name="apply-job"),
    path("withdraw-job-application/", withdraw_job_application, name="withdraw-job-application"),
]