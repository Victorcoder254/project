from django.contrib import admin
from .models import*

@admin.register(Contact_Info)
class Contact_InfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'date')


class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visit_date", "location")


admin.site.register(Visitor, VisitorAdmin)    
