from django.contrib import admin
from .models import*

@admin.register(Contact_Info)
class Contact_InfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'date')


class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visit_date", "location")


admin.site.register(Visitor, VisitorAdmin)

class PricingAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "date")

admin.site.register(Pricing, PricingAdmin)    

class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

admin.site.register(Business, BusinessAdmin)


class Operating_HoursAdmin(admin.ModelAdmin):
    list_display = ("business",)

admin.site.register(OperatingHours, Operating_HoursAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ("business",)

admin.site.register(Service, ServicesAdmin)


class Appointment_Page_Theme_Admin(admin.ModelAdmin):
    list_display = ("business",)


admin.site.register(AppointmentPageTheme, Appointment_Page_Theme_Admin)    
