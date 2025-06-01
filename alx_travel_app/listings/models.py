from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model # To get the User model

# Get the currently active User model, handles custom user models if you ever define one
User = get_user_model()

class Listing(models.Model):
    # Basic Listing Information
    # Using default='' for CharFields to avoid null values and migration prompts
    title = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    zipcode = models.CharField(max_length=20, default='')
    description = models.TextField(blank=True) # blank=True means it's optional in forms/admin

    # Numerical Listing Details
    # Using default=0 or default=0.0 to avoid null values and migration prompts for numbers
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    sqft = models.IntegerField(default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)

    # Media and Status
    # blank=True and null=True make ImageField optional in forms and database
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(default=True) # Default to true for new listings
    list_date = models.DateTimeField(default=datetime.now, blank=True) # Sets creation time

    # Define how a Listing object is represented (e.g., in the admin)
    def __str__(self):
        return self.title

class Booking(models.Model):
    # Foreign Keys link to other models
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE) # If Listing is deleted, delete Booking
    user = models.ForeignKey(User, on_delete=models.CASCADE) # If User is deleted, delete Booking

    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending') # Default status
    booked_at = models.DateTimeField(auto_now_add=True) # Automatically sets on creation

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user.username}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField() # e.g., 1 to 5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Ensures a user can only review a specific listing once
    class Meta:
        unique_together = ('listing', 'user')

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user.username} - {self.rating} stars" 