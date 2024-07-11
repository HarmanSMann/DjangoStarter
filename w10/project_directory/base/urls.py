from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Add path to route to base page view function
    path('base/', views.base),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('generate_image/', views.generate_image, name="generate_image"),
]
