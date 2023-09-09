from django.shortcuts import render

import csv
import folium
from folium.plugins import FastMarkerCluster

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
    file = '/home/trinitykleckner/Me/pennapps/B4UGo/data/EV_Charging_Stations.csv'
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

load_from_csv()
