# from geopy.geocoders import Nominatim

# def get_location(latitude, longitude):
#     geolocator = Nominatim(user_agent="geoapiExercises")
#     location = geolocator.reverse((latitude, longitude), exactly_one=True)
#     return location.address if location else "Location not found."

# # Latitude aur Longitude input karein
# lat = float(input("Latitude daalein: "))
# lon = float(input("Longitude daalein: "))

# # Location ka pata lagayein
# location = get_location(lat, lon)
# print("Location:", location)
import random

def generate_random_coordinates(num_points):
    coordinates = set()

    while len(coordinates) < num_points:
        # Latitude ranges from -90 to 90
        latitude = random.uniform(-90, 90)
        # Longitude ranges from -180 to 180
        longitude = random.uniform(-180, 180)
        
        # Add the (latitude, longitude) tuple to the set
        coordinates.add((round(latitude, 6), round(longitude, 6)))

    return list(coordinates)

# Specify the number of unique points you want
num_points = 1
unique_coordinates = generate_random_coordinates(num_points)

for coord in unique_coordinates:
    print(coord)