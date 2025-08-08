import pandas as pd
import requests
from optimizer_simulator.visualizer import print_map
from optimizer_simulator.algo import find_best_path
import folium

def load_points(file_path):
    csv = pd.read_csv(file_path)
    return csv

def get_data(points):
    url = "http://router.project-osrm.org/table/v1/driving/"
    coords = ";".join([f"{p[2]},{p[1]}" for p in points.values])
    url = url + coords
    params={
        "annotations": "distance,duration"
    }

    response = requests.get(url, params=params)
    data = response.json()
    if 'distances' not in data:
        raise ValueError("Error: Wrong response- no data")

    best_path = find_best_path(data['distances'])
    coords = [data['destinations'][i]['location'] for i in best_path]

    return coords,best_path




