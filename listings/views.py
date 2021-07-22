from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing


# Index
def index(response):
    listings = Listing.objects.all()

    return render(response, 'listings/archive.html', {"listings": listings})


# Single Listing
def single(response, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
 
    return render(response, 'listings/single.html', {"listing": listing})
