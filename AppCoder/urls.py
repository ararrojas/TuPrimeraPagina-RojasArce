from django.contrib import admin
from django.urls import path

from.views import cursos_view, inicio_view


urlpatterns = [
    path("inicio/", inicio_view),
    path("cursos/", cursos_view),
]
