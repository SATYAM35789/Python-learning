


# import geocoder

# # Get the current location
# g = geocoder.ip('me')

# # Print latitude and longitude
# print(f"Latitude: {g.latlng[0]}")
# print(f"Longitude: {g.latlng[1]}")

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
import folium
from folium.plugins import MarkerCluster

# Function to create a map
def create_map():
    # Map ka center (default location)
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # India ka center

    # Marker cluster add karte hain
    marker_cluster = MarkerCluster().add_to(m)

    # Click event ke liye function
    def add_lat_lon(event):
        lat = event.latlng['lat']
        lon = event.latlng['lng']
        folium.Marker(location=[lat, lon], popup=f'Latitude: {lat}, Longitude: {lon}').add_to(marker_cluster)

    # Map ko save karein
    m.save('interactive_map.html')
    return m

# Map banayein
my_map = create_map()

# Map ka HTML file kholne ke liye
import webbrowser
webbrowser.open('interactive_map.html')
