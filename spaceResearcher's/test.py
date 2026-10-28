# import random
# import math

# R = 6371.0  # Earth radius in kilometers

# def generate_random_coordinates(num_points):
#     coordinates = set()

#     while len(coordinates) < num_points:
#         # Latitude ranges from -90 to 90
#         latitude = random.uniform(-90, 90)
#         # Longitude ranges from -180 to 180
#         longitude = random.uniform(-180, 180)
        
#         # Add the (latitude, longitude) tuple to the set
#         coordinates.add((round(latitude, 6), round(longitude, 6)))

#     return list(coordinates)

# # Specify the number of unique points you want
# num_points = 1
# unique_coordinates = generate_random_coordinates(num_points)

# for coord in unique_coordinates:
#     latitude, longitude = coord  # Extract latitude and longitude
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)


# def haversine(lat1, lon1, lat2, lon2):
#     """
#     Calculate the distance between two points on a sphere (such as the Earth)
#     using the Haversine formula.
#     """
#     dlat = math.radians(lat2 - lat1)  # Convert degrees to radians
#     dlon = math.radians(lon2 - lon1)  # Convert degrees to radians

#     a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
#     c = 2 * math.asin(math.sqrt(a))

#     return R * c  # Distance in kilometers

# def main():
#     user_lat = float(input("Enter your latitude: "))
#     user_lon = float(input("Enter your longitude: "))

#     target_lat = float(latitude)
#     target_lon = float(longitude)

#     distance = haversine(user_lat, user_lon, target_lat, target_lon)
#     print(f"The distance is {distance:.2f} kilometers.")

# if __name__ == "__main__":
#     main()
from flask import Flask, jsonify, request
import random
import math

app = Flask(__name__)

R = 6371.0  # Earth radius in kilometers

def generate_random_coordinates(num_points):
    coordinates = set()
    while len(coordinates) < num_points:
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        coordinates.add((round(latitude, 6), round(longitude, 6)))
    return list(coordinates)

def haversine(lat1, lon1, lat2, lon2):
    dlat = math.radians(lat2 - lat1)  # Convert degrees to radians
    dlon = math.radians(lon2 - lon1)  # Convert degrees to radians

    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))

    return R * c  # Distance in kilometers

@app.route('/generate_coordinates', methods=['GET'])
def generate_coordinates():
    num_points = request.args.get('num_points', default=1, type=int)
    unique_coordinates = generate_random_coordinates(num_points)
    return jsonify(unique_coordinates)

@app.route('/calculate_distance', methods=['POST'])
def calculate_distance():
    data = request.get_json()
    user_lat = data['user_lat']
    user_lon = data['user_lon']
    target_lat = data['target_lat']
    target_lon = data['target_lon']

    distance = haversine(user_lat, user_lon, target_lat, target_lon)
    return jsonify({"distance": distance})

if __name__ == '__main__':
    app.run(debug=True)
