from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.db import transaction
from datetime import timedelta
from decimal import Decimal, InvalidOperation

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
    if request.method == "POST":
        try:
            # Check if user already exists
            existing_user = User.objects.filter(email=request.POST.get("email")).first()
            if existing_user:
                return JsonResponse({"error": "User already exists."}, status=400)

            with transaction.atomic():
                # Admin User Details
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                password = request.POST.get("password")
                confirm_password = request.POST.get("confirm_password")

                if password != confirm_password:
                    return JsonResponse({"error": "Passwords do not match."}, status=400)

                admin_user = User.objects.create_user(
                    username=request.POST.get("email"),
                    email=request.POST.get("email"),
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                # Business Details
                business = Business.objects.create(
                    user=admin_user,
                    name=request.POST.get("name"),
                    email=request.POST.get("email"),
                    phone_number=request.POST.get("phone_number"),
                    whatsapp_number=request.POST.get("whatsapp_number"),
                    country=request.POST.get("country"),
                    location=request.POST.get("location"),
                    type_of_business=request.POST.get("type_of_business"),
                    description=request.POST.get("description")
                )

                # Operating Hours
                operating_hours = OperatingHours.objects.create(
                    business=business,
                    weekday_opening_time=request.POST.get("weekday_opening_time"),
                    weekday_closing_time=request.POST.get("weekday_closing_time"),
                    max_appointments_per_day=request.POST.get("max_appointments"),
                    operates_weekends=request.POST.get("operates_weekends") == "true",
                    saturday_opening_time=request.POST.get("saturday_opening_time"),
                    saturday_closing_time=request.POST.get("saturday_closing_time"),
                    sunday_opening_time=request.POST.get("sunday_opening_time"),
                    sunday_closing_time=request.POST.get("sunday_closing_time"),
                    operates_public_holidays=request.POST.get("operates_public_holidays") == "true",
                    public_holiday_opening_time=request.POST.get("public_holiday_opening_time"),
                    public_holiday_closing_time=request.POST.get("public_holiday_closing_time")
                )

            # Services data processing
            service_names = request.POST.getlist("service_name[]")
            service_descriptions = request.POST.getlist("service_description[]")
            service_duration_hours = request.POST.getlist("service_duration_hours[]")
            service_duration_minutes = request.POST.getlist("service_duration_minutes[]")
            service_prices = request.POST.getlist("service_price[]")

            print(f"Service names: {service_names}")
            print(f"Service descriptions: {service_descriptions}")
            print(f"Service durations (hours): {service_duration_hours}")
            print(f"Service durations (minutes): {service_duration_minutes}")
            print(f"Service prices: {service_prices}")

            # Handle creation of multiple services in a single transaction
            # Handle creation of multiple services in a single transaction
            services_to_create = []
            for i in range(len(service_names)):
                  try:
                        # Ensure valid duration (hours and minutes)
                        duration_hours = int(service_duration_hours[i] or 0)  # Default to 0 if not valid
                        duration_minutes = int(service_duration_minutes[i] or 0)  # Default to 0 if not valid

                        # Special case for "00" as minute input
                        if service_duration_minutes[i] == "00":
                              duration_minutes = 0  # Force it to 0 if the value is "00"

                        # Create the timedelta object with the validated values
                        duration = timedelta(hours=duration_hours, minutes=duration_minutes)

                        # Clean price input (remove extra spaces, ensure proper formatting)
                        price_str = service_prices[i].strip()  # Remove whitespace
                        try:
                              price = Decimal(price_str) if price_str else None
                        except InvalidOperation:
                              print(f"Invalid price value for service {i+1}: {price_str}")
                              return JsonResponse({"error": f"Invalid price value for service {i+1}"}, status=400)

                        # Append service creation to list
                        services_to_create.append(Service(
                              business=business,
                              name=service_names[i],
                              description=service_descriptions[i],
                              duration=duration,
                              price=price
                        ))

                  except ValueError as ve:
                        # Log specific error for invalid duration
                        print(f"Error processing duration for service {i+1}: {ve}")
                        return JsonResponse({"error": f"Invalid duration values for service {i+1}"}, status=400)
                  except Exception as e:
                        # Log any other unexpected errors
                        print(f"Error processing service {i+1}: {e}")
                        return JsonResponse({"error": f"An unexpected error occurred for service {i+1}"}, status=500)

            # Bulk create all services, ensuring we ignore conflicts with unique constraints
            if services_to_create:
                  try:
                        Service.objects.bulk_create(services_to_create, ignore_conflicts=True)  # This ensures that if duplicate names exist, they are ignored
                        print(f"Total services created: {len(services_to_create)}")
                  except Exception as e:
                        print(f"Error during bulk create: {e}")
                        return JsonResponse({"error": "Failed to create all services."}, status=500)
                  else:
                        print("No services to create.")  # Handle case where no services are being passed


            # Redirect after all services are created
            return redirect("home")

        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            print(f"Unexpected error: {e}")  # Log unexpected errors for better debugging
            return JsonResponse({"error": "An unexpected error occurred."}, status=500)

    return render(request, "files/onboarding.html")


def start(request, pk):
    business = Business.objects.get(pk=pk)
    context = {
        "business": business,
    }
    return render(request, "files/start.html", context)


def choose_appointment(request, pk):
    business = Business.objects.get(pk=pk)
    services = Service.objects.filter(business=business)  # Fetch all services for this business
    context = {
        "business": business,
        "services": services,
    }
    return render(request, "files/choose_appoinment.html", context)    


def choose_appointment_date(request, business_pk, service_pk):
    business = Business.objects.get(pk=business_pk)
    service = Service.objects.get(pk=service_pk)  # Get the specific service
    context = {
        "business": business,
        "service": service,  # Pass the selected service
    }
    return render(request, "files/choose_appointment_date.html", context)



def our_first_availability(request, business_pk, service_pk): # Get the first available date
    business = Business.objects.get(pk=business_pk)
    service = Service.objects.get(pk=service_pk)  # Get the specific service
    context = {
        "business": business,
        "service": service,  # Pass the selected service
    }
    return render(request, "files/our_first_availability.html", context)



def lets_schedule(request, business_pk, service_pk):# book appointment
    business = Business.objects.get(pk=business_pk)
    service = Service.objects.get(pk=service_pk)  # Get the specific service
    context = {
        "business": business,
        "service": service,  # Pass the selected service
    }
    return render(request, "files/lets_schedule.html", context)



def confirmation(request): # confirmation page
    return render(request, "files/confirmation.html")




def other_options(request): # get another appointment date
    return render(request, "files/other_options.html")


    

   