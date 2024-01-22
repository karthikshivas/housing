from django.contrib import admin
from .models import Listing, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class ListingAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('id', 'title', 'price', 'list_date', 'realtor', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)