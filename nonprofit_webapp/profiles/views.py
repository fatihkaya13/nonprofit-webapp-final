from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponse("welcome to profiles app")

@login_required
def my_home_page_view(request):
    # get profile for requested user
    is_not_found = False
    profile = None
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        is_not_found = True
    # create a form instance from Profile model with related fields
    p_form = ProfileModelForm(request.POST or None,
    request.FILES or None,
    instance=profile)


    # flag to hold whether Profile form is saved or not
    is_p_form_saved = False

    if request.method == "POST":
        if p_form.is_valid():
            p_form.save()
            is_p_form_saved = True

    # create a data dictionary to send HTML templates
    data = {
        "profile": profile,
        "p_form": p_form,
        "is_p_form_saved": is_p_form_saved,
        "is_not_found": is_not_found
    }

    return render(request, "profiles/myprofile.html", data)

@login_required
def my_applied_jobs_view(request):
    is_empty = False
    # get profile for requested user
    my_jobs = Profile.objects.get(user=request.user).applied_job.all()
    is_empty = False if len(my_jobs) > 0 else True
    data = {
        "my_jobs": my_jobs,
        "is_empty": is_empty
    }
    print(data)
    return render(request, "profiles/my_applied_jobs.html", data)
