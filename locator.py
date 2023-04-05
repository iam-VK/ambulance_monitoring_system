import geocoder

def findlocation():
    location = geocoder.ip('me')
    return [location.lat, location.lng]
