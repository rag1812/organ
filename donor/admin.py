from django.contrib import admin
from .models import Donor

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'organ', 'blood_group', 'is_approved')
    list_filter = ('is_approved',)
    actions = ['approve_donors', 'reject_donors']

    def approve_donors(self, request, queryset):
        queryset.update(is_approved=True)

    def reject_donors(self, request, queryset):
        queryset.update(is_approved=False)

admin.site.register(Donor, DonorAdmin)
