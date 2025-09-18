import googlemaps
from utils.config import GOOGLE_MAPS_API_KEY

def plan_shipping_route(origin: str, destination: str, mode: str = "driving") -> str:
    """
    Calculates the distance and estimated travel time between an origin and a destination
    using Google Maps API. Useful for logistics planning.
    """
    if not GOOGLE_MAPS_API_KEY or GOOGLE_MAPS_API_KEY == "your_google_maps_api_key":
        return "Error: Google Maps API key is not configured."
        
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    
    try:
        directions_result = gmaps.directions(origin, destination, mode=mode)
        
        if not directions_result:
            return f"Could not find a route from {origin} to {destination}."

        leg = directions_result[0]['legs'][0]
        distance = leg['distance']['text']
        duration = leg['duration']['text']
        
        return (f"Logistics Plan from {origin} to {destination}:\n"
                f"- Distance: {distance}\n"
                f"- Estimated Duration ({mode}): {duration}")
    except Exception as e:
        return f"An error occurred with Google Maps API: {e}"