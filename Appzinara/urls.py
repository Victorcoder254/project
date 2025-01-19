from django.urls import path 
from .views import *

urlpatterns = [
      path('', home, name='home'),
      path('onboarding/', onboarding, name='onboarding'),
      path('1/<str:pk>/', start, name='start'),
      path('2/<str:pk>/', choose_appointment, name='choose_appointment'),
      path('3/<str:business_pk>/<str:service_pk>/', choose_appointment_date, name='choose_appointment_date'),
      path('4/<str:business_pk>/<str:service_pk>/', our_first_availability, name='our_first_availability'),
      path('5/<str:business_pk>/<str:service_pk>/', lets_schedule, name='lets_schedule'),
      path('6/', other_options, name='other_options'),
]