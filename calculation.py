import geopy.distance
import json

# Starting point (longitude, latitude)
start_point = (0, 0)

# Number of points
num_points = 10

# Distance between points in kilometers
distance_km = 1000

# Generate points
points = [start_point]
current_point = start_point

for _ in range(1, num_points):
    # Calculate next point, 90 degrees from the last to keep moving east
    next_point = geopy.distance.geodesic(kilometers=distance_km).destination(current_point, bearing=90)
    points.append((next_point.longitude, next_point.latitude))
    current_point = (next_point.longitude, next_point.latitude)

# Convert points to GeoJSON format
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": point
            }
        } for point in points
    ]
}

# Save to a file
with open('equidistant_points.geojson', 'w') as f:
    json.dump(geojson, f)

# Add to Mapbox GL JS (this would be in your JavaScript, not Python)
# map.addSource('equidistant-points', {'type': 'geojson', 'data': 'equidistant_points.geojson'})
# map.addLayer({
#     'id': 'equidistant-points-layer',
#     'type': 'circle',
#     'source': 'equidistant-points',
#     'paint': {
#         'circle-radius': 5,
#         'circle-color': '#ff0000'
#     }
# })

