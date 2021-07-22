from django.db import models
from tastypie.resources import ModelResource
from listings.models import Listing


class ListingResource(ModelResource):
    class Meta:
        queryset = Listing.objects.all()
        resource_name = 'listings'
