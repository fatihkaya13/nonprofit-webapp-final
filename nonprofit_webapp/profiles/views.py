from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Jobapplication
from donations.models import Donation
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


    # Create an empty dictionary to store currency sums
    donation_amount_by_currencies = {}

    # Iterate over the list and calculate the sum for each currency
    for item in Donation.objects.filter(user=request.user).all():
        print(item.get_amount())
        print(item.get_currency())
        amount = float(item.get_amount())
        currency = item.get_currency()

        # If the currency key doesn't exist in the dictionary, create it and initialize the sum
        if currency not in donation_amount_by_currencies:
            donation_amount_by_currencies[currency] = amount
        else:
            # If the currency key already exists, add the amount to the existing sum
            donation_amount_by_currencies[currency] += amount



    print(donation_amount_by_currencies)

    # create a data dictionary to send HTML templates
    data = {
        "profile": profile,
        "p_form": p_form,
        "is_p_form_saved": is_p_form_saved,
        "is_not_found": is_not_found,
        "donations_dict": donation_amount_by_currencies
    }

    return render(request, "profiles/myprofile.html", data)

@login_required
def my_applied_jobs_view(request):
    is_empty = False
    # get profile for requested user
    profile = Profile.objects.get(user=request.user)
    my_jobs = Jobapplication.objects.filter(applicant=profile).all()
    is_empty = False if len(my_jobs) > 0 else True
    data = {
        "my_jobs": my_jobs,
        "is_empty": is_empty
    }
    return render(request, "profiles/my_applied_jobs.html", data)


@login_required
def my_donations_view(request):
    is_empty = False
    my_donations = Donation.objects.filter(user=request.user).all()
    is_empty = False if len(my_donations) > 0 else True
    data = {
        "my_donations": my_donations,
        "is_empty": is_empty
    }
    return render(request, "profiles/my_donations.html", data)