from django.urls import path 
from .views import *

urlpatterns = [
      path('', home, name='home'),
      path('onboarding/', onboarding, name='onboarding'),
]