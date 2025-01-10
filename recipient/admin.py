# recipient/admin.py
from django.contrib import admin
from .models import Recipient

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'organ_needed', 'blood_group', 'is_approved')
    list_filter = ('is_approved', 'organ_needed', 'blood_group')
    actions = ['approve_recipients', 'reject_recipients']

    def approve_recipients(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected recipients have been approved.")

    def reject_recipients(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, "Selected recipients have been rejected.")

    approve_recipients.short_description = "Approve selected recipients"
    reject_recipients.short_description = "Reject selected recipients"

admin.site.register(Recipient, RecipientAdmin)
