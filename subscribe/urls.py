from django.urls import path

from subscribe import views


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thankyou/', views.thankyou, name='thank_you'),
]
