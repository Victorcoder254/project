from django.shortcuts import render
from .models import *


def home(request):
      
      # Get Contact Info
      contact_info = Contact_Info.objects.first()
      Pricing_info = Pricing.objects.all()

      context = {
            'contact_info': contact_info,
            'Pricing_info': Pricing_info
      }
      return render(request, 'files/index.html', context)


def onboarding(request):
      return render(request, 'files/onboarding.html')