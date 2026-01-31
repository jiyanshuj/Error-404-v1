import requests
from math import radians, cos, sin, asin, sqrt

TOMTOM_API_KEY = "f0JJhYQPWKpqr1RBTvCaB6jhZuCJtMSu"
USE_MOCK_API = False  # Set to False to use real Tom Tom API

# Mock location database for testing
MOCK_LOCATIONS = {
    "new york": (40.7128, -74.0060),
    "los angeles": (34.0522, -118.2437),
    "london": (51.5074, -0.1278),
    "paris": (48.8566, 2.3522),
    "mumbai": (19.0760, 72.8777),
    "delhi": (28.7041, 77.1025),
    "pune": (18.5204, 73.8567),
    "bangalore": (12.9716, 77.5946),
    "hyderabad": (17.3850, 78.4867),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "tokyo": (35.6762, 139.6503),
    "sydney": (33.8688, 151.2093),
    "toronto": (43.6532, -79.3832),
    "dubai": (25.2048, 55.2708),
    "aictsl campus": (19.0176, 72.8479),
    "aictsl": (19.0176, 72.8479),
    "kurla": (19.0707, 72.8664),
}

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates using Haversine formula"""
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c  # Radius of earth in kilometers
    return km

def get_coordinates(place_name):
    """
    Fetch latitude and longitude for a given place name
    Returns: tuple (latitude, longitude) or None if not found
    """
    if not place_name:
        return None
    
    place_lower = place_name.lower().strip()
    
    if USE_MOCK_API:
        # Use mock API for testing
        if place_lower in MOCK_LOCATIONS:
            coords = MOCK_LOCATIONS[place_lower]
            print(f"[MOCK API] Found coordinates for '{place_name}': {coords}")
            return coords
        else:
            available = ", ".join(MOCK_LOCATIONS.keys())
            print(f"[MOCK API] Location '{place_lower}' not found in mock database")
            print(f"[MOCK API] Available locations: {available}")
            return None
    else:
        # Use real Tom Tom API
        try:
            url = f"https://api.tomtom.com/search/2/geocode/{place_name}.json"
            params = {"key": TOMTOM_API_KEY, "limit": 1}
            print(f"[API] GET {url}")
            response = requests.get(url, params=params, timeout=5)
            print(f"[API] Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if data.get('results'):
                    position = data['results'][0]['position']
                    coords = (position['lat'], position['lon'])
                    print(f"[API] Found coordinates for '{place_name}': {coords}")
                    return coords
                else:
                    print(f"[API] No results found for '{place_name}'")
            else:
                print(f"[API] Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"[API] Request error: {e}")
        except Exception as e:
            print(f"[API] Unexpected error: {e}")
        
        return None

def get_route(start_lat, start_lon, dest_lat, dest_lon):
    """
    Fetch route and distance between two coordinates
    Returns: route data with distance or None if not found
    """
    if USE_MOCK_API:
        # Use mock route calculation
        km = haversine_distance(start_lat, start_lon, dest_lat, dest_lon)
        
        # Generate mock route response matching Tom Tom format
        mock_response = {
            "routes": [
                {
                    "legs": [
                        {
                            "summary": {
                                "lengthInMeters": int(km * 1000),
                                "travelTimeInSeconds": int(km * 50)
                            }
                        }
                    ]
                }
            ]
        }
        print(f"[MOCK API] Route calculated: {km:.2f} km")
        return mock_response
    else:
        # Use real Tom Tom API
        try:
            url = f"https://api.tomtom.com/routing/1/calculateRoute/{start_lat},{start_lon}:{dest_lat},{dest_lon}/json"
            params = {"key": TOMTOM_API_KEY, "routeType": "fastest", "traffic": "false"}
            print(f"[API] GET {url}")
            response = requests.get(url, params=params, timeout=5)
            print(f"[API] Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"[API] Route data received successfully")
                return data
            else:
                print(f"[API] Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"[API] Request error: {e}")
        except Exception as e:
            print(f"[API] Unexpected error: {e}")
        
        return None
