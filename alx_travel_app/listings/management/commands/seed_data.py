import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from listings.models import Listing, Booking, Review

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with dummy data for listings, bookings, and reviews.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))

        # --- Create or get a default user ---
        # Try to get an existing user, or create one if it doesn't exist.
        # Make sure this username and password is what you created via createsuperuser
        try:
            user = User.objects.get(username='admin') # Or your superuser username
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING('Default user (admin) not found. Creating one...'))
            user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='adminpassword' # CHANGE THIS TO A SECURE PASSWORD FOR REAL USE!
            )
            self.stdout.write(self.style.SUCCESS('Default user (admin) created.'))
        self.stdout.write(self.style.SUCCESS(f'Using user: {user.username}'))


        # --- Seed Listings ---
        self.stdout.write(self.style.MIGRATE_HEADING('Seeding Listings...'))
        listings_data = [
            {
                'title': 'Luxury Beach House', 'address': '123 Ocean Dr', 'city': 'Malibu',
                'state': 'CA', 'zipcode': '90265', 'description': 'Stunning ocean views.',
                'price': 1500.00, 'bedrooms': 4, 'bathrooms': 3.5, 'sqft': 3200, 'lot_size': 0.5,
                'is_published': True, 'photo_main': None # Set photo_main to None initially
            },
            {
                'title': 'Cozy Mountain Cabin', 'address': '456 Pine Ln', 'city': 'Aspen',
                'state': 'CO', 'zipcode': '81611', 'description': 'Perfect for winter sports.',
                'price': 500.00, 'bedrooms': 2, 'bathrooms': 1.0, 'sqft': 1200, 'lot_size': 1.2,
                'is_published': True, 'photo_main': None
            },
            {
                'title': 'Downtown Loft', 'address': '789 City Rd', 'city': 'New York',
                'state': 'NY', 'zipcode': '10001', 'description': 'Modern living in the heart of the city.',
                'price': 800.00, 'bedrooms': 1, 'bathrooms': 1.0, 'sqft': 850, 'lot_size': 0.1,
                'is_published': True, 'photo_main': None
            },
             {
                'title': 'Riverside Retreat', 'address': '101 Riverbend', 'city': 'Austin',
                'state': 'TX', 'zipcode': '78704', 'description': 'Peaceful home by the water.',
                'price': 750.00, 'bedrooms': 3, 'bathrooms': 2.0, 'sqft': 1800, 'lot_size': 0.7,
                'is_published': True, 'photo_main': None
            },
            {
                'title': 'Desert Oasis Villa', 'address': '222 Cactus Way', 'city': 'Palm Springs',
                'state': 'CA', 'zipcode': '92262', 'description': 'Luxurious desert getaway with pool.',
                'price': 1200.00, 'bedrooms': 5, 'bathrooms': 4.0, 'sqft': 4000, 'lot_size': 1.0,
                'is_published': True, 'photo_main': None
            },
        ]

        listings = []
        for data in listings_data:
            listing = Listing.objects.create(**data)
            listings.append(listing)
            self.stdout.write(self.style.SUCCESS(f'Created Listing: {listing.title}'))

        # --- Seed Bookings ---
        self.stdout.write(self.style.MIGRATE_HEADING('Seeding Bookings...'))
        for i in range(5):
            listing = random.choice(listings)
            check_in = timezone.now().date() + timezone.timedelta(days=random.randint(1, 30))
            check_out = check_in + timezone.timedelta(days=random.randint(3, 10))
            total_price = listing.price * (check_out - check_in).days
            booking = Booking.objects.create(
                listing=listing,
                user=user,
                check_in_date=check_in,
                check_out_date=check_out,
                total_price=total_price,
                status=random.choice(['Pending', 'Confirmed', 'Cancelled'])
            )
            self.stdout.write(self.style.SUCCESS(f'Created Booking for {listing.title} ({booking.status})'))

        
        # --- Seed Reviews ---
        self.stdout.write(self.style.MIGRATE_HEADING('Seeding Reviews...'))
        # Create one review for each listing using the same user
        for listing in listings: # This loop variable 'listing' is what you should use!
            # Ensure the user has booked this listing to make sense, though not strictly enforced by models now
            review = Review.objects.create(
                listing=listing, # Use the 'listing' from the loop directly
                user=user,
                rating=random.randint(1, 5),
                comment=f"This is a random comment for {listing.title}. Rating: {random.randint(1, 5)} stars."
            )
            self.stdout.write(self.style.SUCCESS(f'Created Review for {listing.title} ({review.rating} stars)'))

        self.stdout.write(self.style.SUCCESS('\nDatabase seeding complete!'))