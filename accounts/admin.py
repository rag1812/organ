from django.contrib import admin
from .models import UserProfile  # Replace with your model

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
