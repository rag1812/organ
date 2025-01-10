from django.urls import path
from . import views

urlpatterns = [
    path('', views.donor_redirect, name='donor_redirect'),  # Main redirect logic
    path('new/', views.new_donor, name='new_donor'),  # New donor registration form
    path('details/', views.donor_details, name='donor_details'),  # Donor details page
]
