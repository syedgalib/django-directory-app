from django.contrib import admin
from .models import Taxonomy, Term


class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    exclude = ('created_at',)

    prepopulated_fields = {'slug': ('title',)}


class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'taxonomy_id', 'slug')
    exclude = ('created_at',)

    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(Term, TermAdmin)
