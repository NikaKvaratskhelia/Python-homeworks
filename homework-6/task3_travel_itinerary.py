locations = [
    ("Tbilisi", 41.71, 44.82),
    ("Batumi", 41.64, 41.63),
    ("Kutaisi", 42.26, 42.71)
]

for city, lat, lon in locations:
    print(f"City: {city}, Latitude: {lat}, Longitude: {lon}")

city_names = [city for city, lat, lon in locations]
print(f"City names list: {city_names}")
