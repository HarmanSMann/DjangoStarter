from django.urls import path
from . import views
urlpatterns = [
    path('', views.movies, name="homepage"),
    path('movie/<str:pk>/', views.movie, name="movie"),
]