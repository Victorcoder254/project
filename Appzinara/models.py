from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.contrib.auth.models import User


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
    

#ONBOARDING MODELS
#
#
#
############################################################################################################


#Business details
# This model will be used to store the business details

class Business(models.Model):
    #Remember to add the user reference field to the model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="business",blank=True, null=True) 
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    type_of_business = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name} - {self.location}"
 

#Business operating hours
class OperatingHours(models.Model):
    business = models.OneToOneField(Business, on_delete=models.CASCADE, related_name="operating_hours")

    max_appointments_per_day = models.PositiveIntegerField(default=1)

    # Weekday hours
    weekday_opening_time = models.TimeField()
    weekday_closing_time = models.TimeField()

    # Weekend operations
    operates_weekends = models.BooleanField(default=False)
    saturday_opening_time = models.TimeField(blank=True, null=True)
    saturday_closing_time = models.TimeField(blank=True, null=True)
    sunday_opening_time = models.TimeField(blank=True, null=True)
    sunday_closing_time = models.TimeField(blank=True, null=True)

    # Public holiday operations
    operates_public_holidays = models.BooleanField(default=False)
    public_holiday_opening_time = models.TimeField(blank=True, null=True)
    public_holiday_closing_time = models.TimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.business.name}: "
            f"Weekdays {self.weekday_opening_time} - {self.weekday_closing_time}, "
            f"Weekends {'Open' if self.operates_weekends else 'Closed'}, "
            f"Public Holidays {'Open' if self.operates_public_holidays else 'Closed'}"
        )

#Business services
 
class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(help_text="Duration of the service (e.g., 00:30:00 for 30 minutes)")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional: Include pricing

    def __str__(self):
        return f"{self.name} - {self.business.name}"



#END OF ONBOARDING MODELS ############################################################################################################