from re import A
from django.contrib import admin

from listings.models import Band

from listings.models import Listing
# Register your models here.


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')
admin.site.register(Band, BandAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'description', 'year')
admin.site.register(Listing, ListingAdmin)
