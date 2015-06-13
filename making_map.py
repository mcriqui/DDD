import time
from geopy.geocoders import GoogleV3
import json

geolocator = GoogleV3()

with open('new_and_imporoved.csv', 'r') as original_file:
    episodes = original_file.read().split('\n')

resources = []

for index, episode in enumerate(episodes):
    episodes[index] = episodes[index].split(',')
    time.sleep(.25)
    season = episodes[index][0]
    title = episodes[index][1]
    restaurant = episodes[index][2]
    city = episodes[index][3]
    state = episodes[index][4]
    business_id = episodes[index][5]
    rating = episodes[index][6]
    number_of_reviews = episodes[index][7]

    try:
        address, (latitude, longitude) = geolocator.geocode(city, state)

        print address, latitude, longitude, rating
    except:
        print "Unable to find location for ", city, state


    else:
        if rating == '5':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "#00CC00",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)
        elif rating == '4.5':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "#00FF00",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)
        elif rating == '4':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "D4FF00",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)
        elif rating == '3.5':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "FFF000",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)

        elif rating == '3':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "#FF9E00",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)

        elif rating == '2.5':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "#BFF4600",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)

        elif rating == '2':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "marker",
                    "marker-color": "#FF0000",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)

        elif rating == 'Closed':
            item = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        longitude,
                        latitude
                    ]
                },
                "properties": {
                    "marker-symbol": "cross",
                    "marker-color": "#000000",
                    "name": restaurant,
                    "rating": rating,
                    "number of reviews": number_of_reviews,
                    "season": season,
                    "episode title": title,
                    "city": city,
                    "state": state,
                }
            }
            resources.append(item)
        else:
            print "something went wrong"

geo = {
    "type": "FeatureCollection",
    "features": resources
}

with open("final_json.json","w") as jsonfile:
    jsonfile.write(json.dumps(geo, indent=4,sort_keys=True))