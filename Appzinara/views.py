from django.shortcuts import render
from .models import *


def home(request):
      
      # Get Contact Info
      contact_info = Contact_Info.objects.first()

      context = {
            'contact_info': contact_info
      }
      return render(request, 'files/index.html', context)
