import geocoder
# import requests
def findlocation():
    location = geocoder.ip('me')
    return [location.lat, location.lng]
# url = "https://nominatim.openstreetmap.org/reverse?format=json&lat={0}&lon={1}".format(location.lat, location.lng)
# response = requests.get(url).json()
#         # extract the address and display it on the console
# address = response["display_name"]
# print(address)