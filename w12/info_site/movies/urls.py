from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name="movies"),
    path('movie/<str:pk>/', views.movie, name="movie"),
    path('add_movie/', views.addMovie, name="add_movie"),
    path('update_movie/<str:pk>/', views.updateMovie, name="update_movie"),
    # Route to delete movie
    path('delete_movie/<str:pk>/', views.deleteMovie, name="delete_movie"),
]
