# Listings App

This Django application (`listings`) is a core component of the ALX Travel App project. It is responsible for managing all data related to travel property listings, user bookings, and reviews.

## Table of Contents

-   [Purpose](#purpose)
-   [Models](#models)
-   [Serializers](#serializers)
-   [Management Commands](#management-commands)
-   [Admin Integration](#admin-integration)
-   [API Endpoints (Planned)](#api-endpoints-planned)

## Purpose

The `listings` app provides the data backbone for the travel application. It defines the structure for properties available for booking, tracks user bookings, and stores feedback through reviews.

## Models

The following database models are defined within this app:

1.  **`Listing`**: Represents a single travel property.
    -   `title`: Name of the property.
    -   `address`, `city`, `state`, `zipcode`: Location details.
    -   `description`: Detailed description of the property.
    -   `price`: Rental price (Decimal).
    -   `bedrooms`, `bathrooms`, `sqft`, `lot_size`: Property specifications.
    -   `photo_main`: Main image for the listing (requires Pillow).
    -   `is_published`: Boolean indicating if the listing is active.
    -   `list_date`: Date and time the listing was created.

2.  **`Booking`**: Represents a reservation made by a user for a specific listing.
    -   `listing` (ForeignKey): Links to the `Listing` model.
    -   `user` (ForeignKey): Links to Django's built-in `User` model.
    -   `check_in_date`, `check_out_date`: Dates of the booking.
    -   `total_price`: Calculated total cost of the booking.
    -   `status`: Current status of the booking (e.g., 'Pending', 'Confirmed', 'Cancelled').
    -   `booked_at`: Timestamp of booking creation.

3.  **`Review`**: Represents a user's review and rating for a listing.
    -   `listing` (ForeignKey): Links to the `Listing` model.
    -   `user` (ForeignKey): Links to Django's built-in `User` model.
    -   `rating`: Numerical rating (e.g., 1-5 stars).
    -   `comment`: Textual feedback from the user.
    -   `created_at`: Timestamp of review creation.
    -   **Constraint:** `unique_together` on `(listing, user)` ensures a user can only submit one review per listing.

## Serializers

Serializers are defined using Django REST Framework to convert model instances into JSON/Python native datatypes and handle validation for incoming data.

-   **`ListingSerializer`**: Serializes `Listing` model data.
-   **`BookingSerializer`**: Serializes `Booking` model data.
-   **`ReviewSerializer`**: Serializes `Review` model data.

These are located in `listings/serializers.py`.

## Management Commands

A custom Django management command is available to facilitate development:

-   **`python manage.py seed_data`**:
    This command clears all existing `Listing`, `Booking`, and `Review` data from the database and then populates it with a set of sample, dummy data. This is useful for quickly setting up a development environment with test data.

    **Usage:**
    ```bash
    python manage.py seed_data
    ```

## Admin Integration

All models (`Listing`, `Booking`, `Review`) are registered with the Django administration site (`listings/admin.py`), allowing for easy CRUD (Create, Read, Update, Delete) operations via the `/admin/` interface.

## API Endpoints (Planned)

This app will be the foundation for the following API endpoints (to be implemented in `listings/views.py` and `listings/urls.py`):

-   `/api/listings/`
-   `/api/listings/<id>/`
-   `/api/bookings/`
-   `/api/bookings/<id>/`
-   `/api/reviews/`
-   `/api/reviews/<id>/`