from rest_framework import serializers
from .models import Listing, Booking, Review # Import your models

# Serializer for the Listing model
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__' # Include all fields from the Listing model

# Serializer for the Booking model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__' # Include all fields from the Booking model

# Serializer for the Review model
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__' # Include all fields from the Review model