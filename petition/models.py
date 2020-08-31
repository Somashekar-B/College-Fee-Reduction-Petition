from django.db import models
from django.urls import reverse
# Create your models here.

Who = (
    ("Student", "Student"),
    ("Staff", "Staff")
)

Year = (
    ("First", "First"),
    ("Second", "Second"),
    ("Third", "Third"),
)

Stay = (
    ("Localite", "Localite"),
    ("Hostalite", "Hostalite"),
)

class PetitionForm(models.Model):
    name = models.CharField(max_length=200, default="Unknown")
    year = models.CharField(max_length=200, choices=Year)
    stay = models.CharField(max_length=100, choices=Stay)
    your_view_about_fee = models.TextField()

    def __str__(self):
        return self.your_view_about_fee

    def get_absolute_url(self):
        return reverse('form')    
