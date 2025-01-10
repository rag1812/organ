# recipient/models.py
from django.db import models
from django.contrib.auth.models import User

# Choices for organs and blood groups (reuse from donor models if shared)
ORGAN_CHOICES = [
    ('kidney', 'Kidney'),
    ('heart', 'Heart'),
    ('lungs', 'Lungs'),
    ('eyes', 'Eyes'),
    ('liver', 'Liver'),
]

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

class Recipient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    organ_needed = models.CharField(max_length=50, choices=ORGAN_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default='O+')
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    is_request_sent = models.BooleanField(default=False)  # Track request status
    is_approved = models.BooleanField(default=False)  # Approval status for admin actions

    def __str__(self):
        return self.name
