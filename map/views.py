import pandas as pd
import json
import requests
from django.shortcuts import render
from django.conf import settings
# Create your views here.


def geocode_address(address, api_key):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': api_key}
    response = requests.get(url, params=params)
    result = response.json()
    if result['status'] == 'OK':
        location = result["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    return None, None


def map_home(request):
    csv_path = (
        '/Users/guns4kids/Downloads/'
        'NorthCarnmarthDeaneryLocationsAndOptions - Sheet1.csv'
    )
    df = pd.read_csv(csv_path)
    api_key = settings.GOOGLE_MAPS_API_KEY

    if 'lat' not in df.columns:
        df['lat'] = None
    if 'lng' not in df.columns:
        df['lng'] = None

    # Lat Lng Cols
    updated = False
    for idx, row in df.iterrows():
        if pd.isna(row['lat']) or pd.isna(row['lng']):
            address = f'{row["Address"]}, {row["Postcode"]}'
            lat, lng = geocode_address(address, api_key)
            df.at[idx, 'lat'] = lat
            df.at[idx, 'lng'] = lng
            updated = True

    if updated:
        df.to_csv(csv_path, index=False)

    locations = df.to_dict(orient='records')
    return render(request, 'map/map_home.html', {
        'google_maps_api_key': api_key,
        'locations_json': json.dumps(locations)
    })
