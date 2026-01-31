from django.shortcuts import render, redirect
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
            print(f"[DEBUG] Fetching coordinates for: {current_location}")
            start_coords = get_coordinates(current_location)
            print(f"[DEBUG] Start coords: {start_coords}")
            
            print(f"[DEBUG] Fetching coordinates for: {destination}")
            dest_coords = get_coordinates(destination)
            print(f"[DEBUG] Dest coords: {dest_coords}")

            if not start_coords or not dest_coords:
                error_msg = 'Failed to fetch location coordinates. Please check location names.'
                print(f"[DEBUG] Error: {error_msg}")
                return render(request, 'error.html', {'message': error_msg})

            # Fetch route data
            start_lat, start_lon = start_coords
            dest_lat, dest_lon = dest_coords
            print(f"[DEBUG] Calculating route: ({start_lat},{start_lon}) to ({dest_lat},{dest_lon})")
            route_data = get_route(start_lat, start_lon, dest_lat, dest_lon)
            print(f"[DEBUG] Route data received: {route_data is not None}")

            if not route_data:
                error_msg = 'Failed to fetch route data. Please try again.'
                print(f"[DEBUG] Error: {error_msg}")
                return render(request, 'error.html', {'message': error_msg})

            # Extract distance (in kilometers)
            try:
                legs = route_data.get('routes', [])[0].get('legs', [])
                if legs and len(legs) > 0 and 'summary' in legs[0]:
                    total_distance_km = legs[0]['summary']['lengthInMeters'] / 1000
                else:
                    total_distance_km = 0
                print(f"[DEBUG] Total distance: {total_distance_km} km")
            except (IndexError, KeyError, TypeError) as e:
                print(f"[DEBUG] Error parsing route data: {e}")
                print(f"[DEBUG] Route data structure: {route_data}")
                total_distance_km = 0

            # Store trip details in session for later use
            try:
                request.session['trip_current_location'] = current_location
                request.session['trip_destination'] = destination
                request.session['trip_budget'] = float(budget)
                request.session['trip_distance'] = float(total_distance_km)
            except Exception as e:
                print(f"[DEBUG] Error storing session data: {e}")

            # Convert to float for template comparisons
            total_distance_float = float(total_distance_km)
            
            print(f"[DEBUG] Rendering success page with distance: {total_distance_float}")
            print(f"[DEBUG] Distance type: {type(total_distance_float)}")
            print(f"[DEBUG] Context data: current_location={current_location}, destination={destination}, budget={budget}, distance={total_distance_float}")
            
            # Render success page with trip details
            try:
                return render(
                    request,
                    'success.html',
                    {
                        'current_location': current_location,
                        'destination': destination,
                        'budget': float(budget),
                        'distance': total_distance_float,
                    }
                )
            except Exception as e:
                print(f"[DEBUG] ERROR rendering template: {e}")
                import traceback
                traceback.print_exc()
                error_msg = f'Error rendering success page: {str(e)}'
                return render(request, 'error.html', {'message': error_msg})
        else:
            # Form validation failed
            print(f"[DEBUG] Form validation failed: {form.errors}")
            return render(request, 'trip_form.html', {'form': form})
    else:
        form = TripForm()

    return render(request, 'trip_form.html', {'form': form})

def final(request):
    """Hotel booking page - displays available hotels"""
    return render(request, 'booking.html')

def payment(request):
    """Booking details form page"""
    if request.method == 'POST':
        # Store booking details in session
        request.session['booking_first_name'] = request.POST.get('firstName')
        request.session['booking_last_name'] = request.POST.get('lastName')
        request.session['booking_email'] = request.POST.get('email')
        request.session['booking_phone'] = request.POST.get('phone')
        request.session['booking_address'] = request.POST.get('address')
        return redirect('pay')
    
    return render(request, 'form.html')

def pay(request):
    """Payment page"""
    return render(request, 'payment.html')

def booking_success(request):
    """Final booking success page"""
    context = {
        'booking_id': 'BK' + request.session.get('booking_email', 'GUEST')[:8].upper(),
        'guest_name': request.session.get('booking_first_name', 'Guest') + ' ' + request.session.get('booking_last_name', ''),
        'guest_email': request.session.get('booking_email', 'N/A'),
    }
    return render(request, 'booking_success.html', context)
