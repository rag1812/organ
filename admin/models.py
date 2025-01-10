from django.db import models

from donor.models import Donor
from recipient.models import Recipient

# Create your models here.
class OrganRequest(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')  # Pending, Approved, Denied

    def __str__(self):
        return f"Request: {self.recipient.name} -> {self.donor.name}"
