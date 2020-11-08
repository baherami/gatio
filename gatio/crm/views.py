from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required
def index(request):
    user = request.user
    if user.groups.first() == "machine":
        return HttpResponse(f"Welcome my son.")
    return HttpResponse(f"Hello, {user} . You're at the index.")


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("logged in.")
    else:
        return HttpResponse("invalid.")


def logout_view(request):
    logout(request)
    return HttpResponse("logged out.")


# broad cast
@login_required
def get_next_batch(request):
    user = request.user
    #match =
    return HttpResponse("get_next.")


def match_make(request):
    return HttpResponse("matchmake.")


def profile(request):
    return HttpResponse("profile.")


