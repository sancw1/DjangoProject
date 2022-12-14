from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('film', views.filmPage),
    path('Search', views.Search),
    path('Genre', views.Genre),
    path('Admin', views.Admin),
    path('CloseAdmin', views.AdminClose),
    path('ChangeFilmDetail', views.ChangeFilmDetails),
    path('DeleteFilm', views.DeleteFilm),
    path('AddFilmPage', views.AddFilmPage),
    path('AddFilm', views.AddFilm),
]