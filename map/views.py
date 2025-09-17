import pandas as pd
import json
import os
import requests
from django.shortcuts import render
from django.conf import settings


def geocode_address(address, api_key):
    """Geocode an address using Google Maps API"""
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': api_key}
    try:
        response = requests.get(url, params=params)
        result = response.json()
        if result['status'] == 'OK':
            location = result["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
    except (requests.RequestException, KeyError, IndexError):
        pass
    return None, None


def map_home(request):
    # Use proper path resolution
    csv_path = os.path.join(settings.BASE_DIR, 'docs', 'NorthCarnmarthDeaneryLocations.csv')
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        return render(request, 'map/map_home.html', {
            'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
            'locations_json': json.dumps([])
        })
    
    api_key = settings.GOOGLE_MAPS_API_KEY

    # Filter valid locations and convert to list
    locations = []
    for _, row in df.iterrows():
        try:
            # Use Latitude/Longitude columns (which have data) instead of lat/lng
            lat = float(row['Latitude']) if not pd.isna(row['Latitude']) else None
            lng = float(row['Longitude']) if not pd.isna(row['Longitude']) else None
            
            if lat and lng:  # Only include valid coordinates
                locations.append({
                    'Name': str(row['Name']),
                    'Location': str(row['Location']),
                    'Postcode': str(row['Postcode']),
                    'lat': lat,
                    'lng': lng
                })
        except (ValueError, TypeError):
            continue  # Skip invalid rows

    return render(request, 'map/map_home.html', {
        'google_maps_api_key': api_key,
        'locations_json': json.dumps(locations)
    })
