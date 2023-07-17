from django.urls import path
from app import views


urlpatterns = [
    path('', views.job_list, name='home-page'),
    path('hello/', views.hello, name='hello'),
    path('jobs/<int:id>', views.job_details, name='product-details'),
    path('jobs/<str:id>', views.job_details, name='product-details')
]
