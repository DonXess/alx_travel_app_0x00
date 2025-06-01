# ALX Travel App (Django REST API)

This project is a backend RESTful API for a travel application, built with Django and Django REST Framework. It manages listings for travel properties, bookings, and user reviews.

## Table of Contents

-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Setup Instructions](#setup-instructions)
    -   [Prerequisites](#prerequisites)
    -   [Clone the Repository](#clone-the-repository)
    -   [Virtual Environment Setup](#virtual-environment-setup)
    -   [Install Dependencies](#install-dependencies)
    -   [Environment Variables (.env)](#environment-variables-env)
    -   [Database Migrations](#database-migrations)
    -   [Create Superuser](#create-superuser)
    -   [Seed Initial Data](#seed-initial-data)
-   [Running the Application](#running-the-application)
-   [API Endpoints (To be Implemented)](#api-endpoints-to-be-implemented)
-   [Database](#database)
-   [Author](#author)

## Features

-   **Listings Management:** Create, read, update, and delete travel property listings.
-   **Booking System:** Handle bookings for properties, linking users to specific listings and dates.
-   **Review System:** Allow users to submit reviews and ratings for listings.
-   **Django Admin Integration:** Fully manageable data models via the Django administration interface.
-   **RESTful API:** Exposes data through well-defined API endpoints (future development).
-   **Secure Configuration:** Uses environment variables for sensitive settings.

## Technologies Used

-   **Python 3.x**
-   **Django 5.x**
-   **Django REST Framework 3.x**
-   **SQLite3** (for development database)
-   **Pillow** (for image handling in Django models)
-   **django-environ** (for environment variable management)
-   **django-cors-headers** (for Cross-Origin Resource Sharing)

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Ensure you have Python 3.x and `pip` installed on your system.

### Clone the Repository

(Assuming this project will be hosted on a Git repository)

```bash
git clone <repository_url>
cd alx_travel_app