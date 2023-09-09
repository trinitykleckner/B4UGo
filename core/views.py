from django.shortcuts import render

import csv
import folium
from folium.plugins import FastMarkerCluster
import requests as r

# Create your views here.
def index(request):

    places = load_from_csv()
    map = folium.Map(location=[41.5025, -72.699997], zoom_start=9)
    latitudes = [place['latitude'] for place in places]
    longitudes = [place['longitude'] for place in places]
    FastMarkerCluster(data = list(zip(latitudes,longitudes))).add_to(map)

    # for place in places:
    #     coords = (place['latitude'], place['longitude'])
    #     folium.Marker(coords).add_to(map) #CAN ADD POPUP HERE folium Marker Docs for details

    context = {'map': map._repr_html_()}
    return render(request, 'index.html', context)

def load_from_csv():
    file = 'data/EV_Charging_Stations.csv'
    keys = ('Station Name', 'New Georeferenced Column')
    records = []

    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append({key: row[key] for key in keys})

    for record in records:
        longitude, latitude = record[keys[1]].split("(")[-1].split(")")[0].split()
        record['longitude'] = float(longitude)
        record['latitude'] = float(latitude)
    print(records)

    return records

mapbox_api_token = 'pk.eyJ1IjoidGtoYXYiLCJhIjoiY2xtYmRmcHh0MTA1MzN0czVoOTR2YTRucSJ9.AVSquDkpzPKthwGBk0sByg'
session_id = '0ac69c5a-92d6-4f18-8a7a-36c99d067a9a'

def get_categories():
    url = 'https://api.mapbox.com/search/searchbox/v1/list/category?&access_token='+mapbox_api_token
    categories = [category['canonical_id'] for category in r.get(url).json()['listItems']]
    categories.remove('gun_store')
    return categories

def category_search(category_id, long, lat):
    url = 'https://api.mapbox.com/search/searchbox/v1/category/'+category_id+'limit=25&proximity='+str(long)+','+str(lat)+'&access_token='+mapbox_api_token
    print(url)
    results = r.get(url).json()
    print(results)
    pass

def search(search_obj_id):
    url = 'https://api.mapbox.com/search/searchbox/v1/retrieve/'+search_obj_id+'?session_token='+session_id+'&access_token='+mapbox_api_token

    req = r.get(url)
    print(req.json())
    print(req.json()['features'])

def get_suggestions(input, long, lat):
    coords = str(long)+','+str(lat)
    url = 'https://api.mapbox.com/search/searchbox/v1/suggest?q='+input+'&language=en&proximity='+coords+'&session_token='+session_id+'&access_token='+mapbox_api_token
    suggestions = r.get(url).json()['suggestions']
    # print(suggestions)
    return suggestions[0]['mapbox_id']


id = get_suggestions('foo', -75.3043287827, 40.00583331)
search(id)
