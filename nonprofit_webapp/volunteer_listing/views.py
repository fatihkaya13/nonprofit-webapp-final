from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Job
from profiles.models import Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponse("welcome to volunteer_listing app")

def jobs_list_view(request):
    # get all job instances
    jobs = Job.objects.all()
    # get requested user
    user = request.user
    print(user)
    # get profile of the user
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = None

    # prepare data to render
    data = {
        "jobs": jobs,
        "profile": profile
    }
    return render(request, 'volunteer_listing/job_list.html', data)

def filtered_jobs_list_view(request):
    if request.method == 'GET':
        # get form query parameter
        text_to_search = request.GET.get('job')
        job_not_found = False
    try:
        # query through title and description
        jobs = Job.objects.filter(Q(title__icontains=text_to_search) | Q(description__icontains=text_to_search))
        job_not_found = False if len(jobs) > 0 else True
        data = {
        "jobs": jobs,
        "job_not_found": job_not_found,
    }
    except:
        job_not_found = True
        data = {
        "job_not_found": job_not_found,
        }

    return render(request, 'volunteer_listing/filtered_job_list.html', data)

@login_required
def apply_job(request):
    if request.method == 'POST':
        # get primary key of the requested job
        pk = request.POST.get('job_pk')
        # get requested user
        user = request.user
        # get profile of the user
        profile = Profile.objects.get(user=user)
        # get job instance
        job = Job.objects.get(pk=pk)
        # add job instance to profile's applied jobs
        profile.applied_job.add(job)
        # save profile instance
        profile.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('volunteer-listing:jobs_list_view')

@login_required
def withdraw_job_application(request):

    if request.method=="POST":
        # get primary key of the requested job
        pk = request.POST.get('job_pk')
        # get requested user
        user = request.user
        # get profile of the user
        profile = Profile.objects.get(user=user)
        # get job instance
        job = Job.objects.get(pk=pk)
        # remove job instance to profile's applied jobs
        profile.applied_job.remove(job)
        # save profile instance
        profile.save()

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))
