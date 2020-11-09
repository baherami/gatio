from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

STANDARD_ADVERTISMENT_LENGTH = 20

@login_required
def index(request):
    user = request.user
    if user.groups.first().name == "Machine":
        return get_next_batch(request)
        #return HttpResponse(f"Welcome my son.")
    else:
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
    screen = Screen.objects.get(screen_client=request.user.client)
    screen_owner = screen.screen_owner

    matches = Match.objects.filter(screen_owner=screen_owner)
    if not matches.exists():
         matches = screen_owner.match_make()
         return "array"
    else:
        ad_lengths = 0
        for match in matches:
            advertisor = match.advertiser
            ads = Advertisement.objects.filter(advertisor=advertisor)
            for ad in ads:
                ad_lengths += ad.media_content.media_length
        if ad_lengths < STANDARD_ADVERTISMENT_LENGTH:
            matches = screen_owner.match_make()
            return "array"
    return HttpResponse(matches)


def profile(request):
    return HttpResponse("profile.")


