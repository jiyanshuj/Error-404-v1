import requests

TOMTOM_API_KEY = "f0JJhYQPWKpqr1RBTvCaB6jhZuCJtMSu"

def get_coordinates(place_name):
    url = f"https://api.tomtom.com/search/2/geocode/{place_name}.json"
    params = {"key": TOMTOM_API_KEY, "limit": 1}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            position = data['results'][0]['position']
            return position['lat'], position['lon']
    return None

def get_route(start_lat, start_lon, dest_lat, dest_lon):
    url = f"https://api.tomtom.com/routing/1/calculateRoute/{start_lat},{start_lon}:{dest_lat},{dest_lon}/json"
    params = {"key": TOMTOM_API_KEY, "routeType": "fastest", "traffic": "true"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None
