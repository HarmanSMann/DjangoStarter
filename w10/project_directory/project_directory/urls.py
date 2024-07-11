from django.contrib import admin
from django.urls import path, include

# Import HTTP module
from django.http import HttpResponse
from django.shortcuts import render

# View function for homepage
def home(request):
    return (render(request, "homepage.html"))

# View function for about
def about(request):
    return (render(request, "about.html"))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Using the name parameter for better referencing
    path('about/', about, name='about'),  # Added a trailing slash for consistency
    path('base/', include("base.urls")), # Route to base app urls
]
