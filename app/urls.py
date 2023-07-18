from django.urls import path
from app import views


urlpatterns = [
    path('', views.job_list, name='home-page'),
    path('jobs/<str:id>', views.job_details, name='product-details')
]
