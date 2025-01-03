from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.db.models import JSONField


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255, blank=True, null=True)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Visitor {self.ip_address} on {self.visit_date}"
    
    
class Contact_Info(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    # Social Media Links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.phone} - {self.date}" 

class Pricing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.price} - {self.date}"        
    

#Business details
# This model will be used to store the business details

class Business(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
 
    

# Business operating hours
# This model will be used to set the operating hours of the business

class OperatingHours(models.Model):
    DAYS_OF_WEEK = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="operating_hours")
    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.name} - {self.day}: {self.opening_time} to {self.closing_time}" if not self.is_closed else f"{self.business.name} - {self.day}: Closed"
 


#Business appointment Page Theme
# This model will be used to set the theme of the appointment page


class AppointmentPageTheme(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="themes")
    theme_settings = JSONField(blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.name} - Theme"
