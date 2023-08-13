from django.http import HttpResponse
from django.shortcuts import render

def welcome_view(request):
    user = request.user
    hello = "Welcoming message"

    context = {
        "user": user,
        "hello": hello,
    }
    return render(request, "main/welcome.html", context)