# donor/models.py

from django.db import models
from django.contrib.auth.models import User

# Choices for organs
ORGAN_CHOICES = [
    ('kidney', 'Kidney'),
    ('heart', 'Heart'),
    ('lungs', 'Lungs'),
    ('eyes', 'Eyes'),
    ('liver', 'Liver'),
]

# Choices for blood groups
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

class Donor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    
    # Use choices for organ and blood group
    organ = models.CharField(max_length=50, choices=ORGAN_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,default='o+')
    
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255,null=True,blank=True)
    mobile_number = models.CharField(max_length=15,null=True,blank=True)
    is_deceased = models.BooleanField(default=False)
    hiv_status = models.BooleanField(default=False)  # True if HIV positive
    willing_to_donate = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)  # To track approval status

    def __str__(self):
        return self.name
