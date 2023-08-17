from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
# Create your views here.

def index(request):
    return HttpResponse("welcome to volunteer_listing app")

def jobs_list_view(request):
    jobs = Job.objects.all()
    data = {
        "jobs": jobs
    }
    return render(request, 'volunteer_listing/job_list.html', data)
