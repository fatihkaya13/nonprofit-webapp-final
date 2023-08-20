from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import DonationForm

# Create your views here.
def index(request):
    return HttpResponse("welcome to donations app")


@login_required
def donation_form(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            return redirect('donations:donation-success')
    else:
        form = DonationForm()
    return render(request, 'donations/donation_form.html', {'form': form})


@login_required
def donation_success(request):
    return render(request, 'donations/donation_success.html')