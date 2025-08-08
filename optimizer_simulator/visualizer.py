import folium

def print_map(points):
    start_y, start_x = points[0]
    m = folium.Map(location=[start_x, start_y], zoom_start=12)

    for i, (lon, lat) in enumerate(points):
        folium.Marker(
            location=[lat, lon],
            popup=f"Point {i+1}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    folium.PolyLine(locations=[[lat, lon] for lon, lat in points], color="blue").add_to(m)

    m.save("output/map.html")
    print("Map has been saved in location output/map.html")