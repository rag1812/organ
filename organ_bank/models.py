from django.db import models

from donor.models import Donor

# Create your models here.
class OrganBank(models.Model):
    organ = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.organ} ({self.blood_group})"
