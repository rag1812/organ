from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from accounts import views  # Ensure this is importing from the correct app
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),   
    path('donor/', views.donor_page, name='donor'),  # Define donor URL here
    path('recipient/', views.recipient_page, name='recipient'),
]
