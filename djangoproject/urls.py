from django.contrib import admin
from django.urls import path, include
from djangoproject import views 
from .views import home_view
from accounts import views  
from accounts.views import signup_view,profile_view


urlpatterns = [
    
    path('hidden-admin-panel/', admin.site.urls),
    path('',home_view, name='home'),
    path('donor/', include('donor.urls')),
    path('recipient/', include ('recipient.urls')),    
    path('', include('accounts.urls')), 

]
