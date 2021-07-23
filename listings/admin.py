from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    exclude = ('created_at',)

    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Listing, ListingAdmin)
