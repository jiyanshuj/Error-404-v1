from django.shortcuts import render
from .forms import TripForm
from .api import get_coordinates, get_route

def trip_view(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            # Extract form data
            current_location = form.cleaned_data['current_location']
            destination = form.cleaned_data['destination']
            budget = form.cleaned_data['budget']

            # Fetch coordinates
            start_coords = get_coordinates(current_location)
            dest_coords = get_coordinates(destination)

            if not start_coords or not dest_coords:
                return render(request, 'error.html', {'message': 'Failed to fetch location coordinates.'})

            # Fetch route data
            start_lat, start_lon = start_coords
            dest_lat, dest_lon = dest_coords
            route_data = get_route(start_lat, start_lon, dest_lat, dest_lon)

            if not route_data:
                return render(request, 'error.html', {'message': 'Failed to fetch route data.'})

            # Extract distance (in kilometers)
            legs = route_data.get('routes', [])[0].get('legs', [])
            total_distance_km = legs[0]['summary']['lengthInMeters'] / 1000 if legs else None

            return render(
                request,
                'success.html',
                {
                    'current_location': current_location,
                    'destination': destination,
                    'budget': budget,
                    'distance': total_distance_km,
                }
            )
    else:
        form = TripForm()

    return render(request, 'trip_form.html', {'form': form})

def final(request):
    return render(request, 'booking.html')

def payment(request):
    return render(request, 'form.html')

def pay(request):
    return render(request, 'payment.html')
