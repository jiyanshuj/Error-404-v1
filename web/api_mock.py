"""
Mock API for testing - Replace real API calls with test data
Useful for testing the flow without depending on Tom Tom API
"""
import math

# Mock database of locations
MOCK_LOCATIONS = {
    'new york': (40.7128, -74.0060),
    'los angeles': (34.0522, -118.2437),
    'london': (51.5074, -0.1278),
    'paris': (48.8566, 2.3522),
    'mumbai': (19.0760, 72.8777),
    'delhi': (28.7041, 77.1025),
    'pune': (18.5204, 73.8567),
    'bangalore': (12.9716, 77.5946),
    'hyderabad': (17.3850, 78.4867),
    'chennai': (13.0827, 80.2707),
    'kolkata': (22.5726, 88.3639),
    'tokyo': (35.6762, 139.6503),
    'sydney': (-33.8688, 151.2093),
    'toronto': (43.6532, -79.3832),
    'dubai': (25.2048, 55.2708),
    'aictsl campus': (19.0176, 72.8479),
    'aictsl': (19.0176, 72.8479),
    'kurla': (19.0707, 72.8664),
}

def get_coordinates(place_name):
    """
    Mock function to fetch coordinates for a place name
    Returns: tuple (latitude, longitude) or None if not found
    """
    place_lower = place_name.lower().strip()
    
    # Check for exact match
    if place_lower in MOCK_LOCATIONS:
        coords = MOCK_LOCATIONS[place_lower]
        print(f"[MOCK API] Found coordinates for '{place_name}': {coords}")
        return coords
    
    # Check for partial match
    for location_key, coords in MOCK_LOCATIONS.items():
        if location_key in place_lower or place_lower in location_key:
            print(f"[MOCK API] Partial match found for '{place_name}': {coords}")
            return coords
    
    # If no match found, generate random coordinates
    # (In production, return None to show error)
    print(f"[MOCK API] Location '{place_name}' not found in mock database")
    print(f"[MOCK API] Available locations: {', '.join(MOCK_LOCATIONS.keys())}")
    return None

def get_route(start_lat, start_lon, dest_lat, dest_lon):
    """
    Mock function to calculate route between two coordinates
    Returns: route data with distance or None if error
    """
    try:
        # Convert to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [start_lat, start_lon, dest_lat, dest_lon])
        
        # Calculate great circle distance using Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        # Radius of earth in kilometers
        radius_km = 6371
        distance_km = radius_km * c
        distance_meters = distance_km * 1000
        
        print(f"[MOCK API] Calculated distance: {distance_km:.2f} km")
        
        # Return mock route data in Tom Tom format
        return {
            'routes': [{
                'legs': [{
                    'summary': {
                        'lengthInMeters': distance_meters,
                        'travelTimeInSeconds': int(distance_km * 60),  # Rough estimate
                    }
                }]
            }]
        }
    except Exception as e:
        print(f"[MOCK API] Error calculating route: {e}")
        return None

# Test the mock API
if __name__ == "__main__":
    print("=== Testing Mock API ===\n")
    
    # Test 1: Get coordinates
    print("Test 1: Get Coordinates")
    coords1 = get_coordinates("New York")
    coords2 = get_coordinates("London")
    print(f"New York: {coords1}")
    print(f"London: {coords2}\n")
    
    # Test 2: Get route
    print("Test 2: Get Route")
    if coords1 and coords2:
        route = get_route(coords1[0], coords1[1], coords2[0], coords2[1])
        if route:
            distance = route['routes'][0]['legs'][0]['summary']['lengthInMeters'] / 1000
            print(f"Distance from New York to London: {distance:.2f} km\n")
    
    # Test 3: Unknown location
    print("Test 3: Unknown Location")
    coords3 = get_coordinates("Unknown City XYZ")
