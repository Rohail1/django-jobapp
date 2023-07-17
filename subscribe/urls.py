from django.contrib import admin
from django.urls import path

from subscribe import views


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
]
