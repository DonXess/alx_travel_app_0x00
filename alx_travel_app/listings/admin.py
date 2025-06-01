from django.contrib import admin
from .models import Listing, Booking, Review # Import your models

# Register your models here so they appear in the Django admin interface.
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Review)