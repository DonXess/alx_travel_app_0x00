from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# Add your viewsets here, for example:
# router.register('listings', views.ListingViewSet)

app_name = 'listings'

urlpatterns = [
    # Add your API URLs here
    # Example: path('', views.ListingListAPIView.as_view(), name='listing-list'),
]

urlpatterns += router.urls
