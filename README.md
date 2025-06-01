# ALX Travel App

A comprehensive travel accommodation booking platform built with Django and Django REST framework.

## Features

### Core Features

- User authentication and authorization
- Property listings with detailed information
- Booking management system
- Review and rating system
- Search and filter functionality
- Admin dashboard for property management

### Technical Stack

- **Backend**: Django 4.2.10
- **API**: Django REST Framework
- **Database**: MySQL
- **Task Queue**: Celery with RabbitMQ
- **API Documentation**: Swagger/OpenAPI (drf-yasg)
- **CORS**: django-cors-headers
- **Environment Management**: django-environ

## Project Structure

```plaintext
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── asgi.py            # ASGI config
│   └── wsgi.py            # WSGI config
└── listings/              # Listings app
    ├── migrations/        # Database migrations
    ├── management/        # Management commands
    ├── models.py          # Data models
    ├── serializers.py     # API serializers
    ├── admin.py          # Admin interface
    ├── apps.py           # App config
    ├── urls.py           # App URL configuration
    └── views.py          # API views
```

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- RabbitMQ
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd alx_travel_app_0x00
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Copy `.env.example` to `.env` and update the values:

   ```bash
   cp .env.example .env
   ```

5. **Set up the database**

   - Create a MySQL database
   - Update the `DATABASE_URL` in `.env`

6. **Run migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Seed the database (optional)**

   ```bash
   python manage.py seed
   ```

9. **Start the development server**

   ```bash
   python manage.py runserver
   ```

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## Available Endpoints

### Listings

- `GET /api/listings/` - List all active listings
- `POST /api/listings/` - Create a new listing (authenticated)
- `GET /api/listings/{id}/` - Get listing details
- `PUT /api/listings/{id}/` - Update a listing (owner only)
- `DELETE /api/listings/{id}/` - Delete a listing (owner only)

### Bookings

- `GET /api/bookings/` - List user's bookings
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Get booking details
- `PATCH /api/bookings/{id}/status/` - Update booking status (host/owner only)

### Reviews

- `GET /api/listings/{id}/reviews/` - Get reviews for a listing
- `POST /api/listings/{id}/reviews/` - Add a review (authenticated users only)

## Listings App

The Listings app is the core component of the ALX Travel App, handling all property-related functionality.

### Models

1. **Listing**
   - Represents a property available for booking
   - Includes details like title, description, location, price, and amenities
   - Managed by a host (User)

2. **Booking**
   - Represents a reservation made by a guest
   - Links a guest to a listing with specific dates
   - Tracks booking status (PENDING, CONFIRMED, COMPLETED, CANCELLED)

3. **Review**
   - Allows guests to rate and review their stay
   - Linked to both the listing and the specific booking

### Management Commands

- `python manage.py seed [--users N] [--listings M] [--bookings O] [--reviews P]`
  - Populates the database with sample data for testing

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Django settings
DEBUG=True
SECRET_KEY=your-secret-key

# Database settings
DATABASE_URL=mysql://user:password@localhost:3306/dbname

# Allowed hosts
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Celery settings
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ALX PROBackend Dev Program