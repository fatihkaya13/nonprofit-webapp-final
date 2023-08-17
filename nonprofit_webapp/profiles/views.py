from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileModelForm
# Create your views here.

def index(request):
    return HttpResponse("welcome to profiles app")


def my_home_page_view(request):
    # get profile for requested user
    profile = Profile.objects.get(user=request.user)
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
    }

    return render(request, "profiles/myprofile.html", data)