from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing


# Index
def index(response):
    listings = Listing.objects.all()

    return render(response, 'listings/archive.html', {"listings": listings})


# Single Listing
def single(response, slug):
    listing = get_object_or_404(Listing, slug=slug)

    return render(response, 'listings/single.html', {"listing": listing})
