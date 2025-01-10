from django.urls import path
from . import views

urlpatterns = [ 
    path('form/', views.recipient_form, name='recipient_form'),
    path('send_request/<int:recipient_id>/<int:donor_id>/', views.send_request_to_admin, name='send_request'),
]
