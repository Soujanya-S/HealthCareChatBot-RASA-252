import requests
import json

def searchHealthcenter(location):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=hospital%20in%20{}&key=AIzaSyBbKoNaeJO-eJR1Axn3dJqSMgSSIP0PRWw".format(location)
    response = requests.request("GET", url, headers={}, data={})

    places_text = response.text
    places = json.loads(places_text)
    places_arr = places['results']

    healthcenterDetails = ""
    healthcenterDetails = "\nHEALTH CARE CENTRE DETAILS NEAR THE LOCATION PROVIDED:\n\n"
    for place in places_arr:
        types = place['types']
        if "health" in types:
            healthcenterDetails += "Health Care Centre : " + place['name'] + "\n"
            healthcenterDetails += "Address : " + place['formatted_address'] + "\n"
            healthcenterDetails += "Rating : " + str(place['rating']) + "\n"
            healthcenterDetails += "Total ratings : " + str(place['user_ratings_total']) + "\n"
            healthcenterDetails += "\n"
    
    return healthcenterDetails
           

