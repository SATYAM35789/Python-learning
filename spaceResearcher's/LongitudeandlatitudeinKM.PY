# import math

# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371  # Earth radius in kilometers
#     dlat = math.radians(lat2 - lat1)
#     dlon = math.radians(lon2 - lon1)
#     a = math.sin(dlat / 2) * 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * 2
#     c = 2 * math.asin(math.sqrt(a))
#     distance = R * c
#     return distance

# user_lat = float(input("Enter your latitude: "))
# user_lon = float(input("Enter your longitude: "))
# target_lat = float(input("Enter target latitude: "))
# target_lon = float(input("Enter target longitude: "))
# distance = haversine(user_lat, user_lon, target_lat, target_lon)
# print(f"The distance is {distance:.2f} kilometers.")30
import math

R = 6371.0  # Earth radius in kilometers

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on a sphere (such as the Earth)
    using the Haversine formula.
    """
    dlat = math.radians(lat2 - lat1)  # Convert degrees to radians
    dlon = math.radians(lon2 - lon1)  # Convert degrees to radians

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return R * c  # Distance in kilometers

def main():
    user_lat = float(input("Enter your latitude: "))
    user_lon = float(input("Enter your longitude: "))

    target_lat = float(input("Enter target latitude: "))
    target_lon = float(input("Enter target longitude: "))

    distance = haversine(user_lat, user_lon, target_lat, target_lon)
    print(f"The distance is {distance:.2f} kilometers.")

if __name__ == "__main__":
    main()
    



    