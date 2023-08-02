from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from .models import *
import re

# Create your views here.


def index(request):
    listings = Listing.objects.all().order_by("-id")
    for listing in listings:
        listing.tags = listing.tags.split(',')
        print(listing.tags)
    return render(request, "devgigs/index.html", {
        "listings": listings
    })


def show_listing(request, listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        pass

    return render(request, 'devgigs/show.html', {
        "listing": listing
    })


def get_listing(request, listing):
    """Get a single listing from the database"""
    try:
        listing = Listing.objects.get(pk=listing)
    except Listing.DoesNotExist:
        return JsonResponse({"message": "Listing does not exist!"}, status=404)

    return JsonResponse({"listing": listing}, safe=False)


def create_listing(request):
    if request.method == "POST":
        company = request.POST.get("company")
        title = request.POST.get("title")
        location = request.POST.get("location")
        email = request.POST.get("email")
        website = request.POST.get("website")
        tags = request.POST.get("tags")
        logo = request.FILES.get("logo")
        description = request.POST.get("description")

        try:
            listing = Listing.objects.create(user=request.user, email=email, title=title, website=website,
                                             description=description, company=company, tags=tags, location=location, logo=logo)
            listing.save()
            return HttpResponseRedirect(reverse('index'))
        except Listing.DoesNotExist:
            return render(request, "devgigs/index.html", {
                "Oops could not create listing!"
            })


def edit_listing(request, listing_id):
    if request.method == "POST":
        try:
            # Get listing to be updated
            listing = Listing.objects.get(pk=listing_id)

            listing.company = request.POST.get("company")
            listing.title = request.POST.get("title")
            listing.location = request.POST.get("location")
            listing.email = request.POST.get("email")
            listing.website = request.POST.get("website")
            listing.tags = request.POST.get("tags")
            listing.logo = request.FILES["logo"]
            listing.description = request.POST.get("description")

            listing.save()
            return render(request, "devgigs/show.html", {
                "message": "Listing updated successfully!",
                "listing": listing
            })

        except Listing.DoesNotExist:
            return render(request, "devgigs/manage.html", {
                "message": "Oops, could not get listing!"
            })


def delete_listing(request, listing_id):
    if request.method == "GET":
        try:
            listing = Listing.objects.get(pk=listing_id)
            listing.delete()
        except Listing.DoesNotExist:
            return render(request, "devgigs/manage.html", {
                "message": "Listing was not found!"
            })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "devgigs/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "devgigs/login.html")


def manage_view(request):
    listings = Listing.objects.filter(user=request.user).order_by('-id')
    return render(request, 'devgigs/manage.html', {
        "listings": listings
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        # Ensure password matches confirmation
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        if password != confirmation:
            return render(request, "devgigs/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "devgigs/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "devgigs/register.html")
