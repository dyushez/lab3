import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def fmain(acct):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': '100'})
        print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
    except urllib.error.HTTPError:
        return 'There is no user with such name'

    js = json.loads(data)
    with open('twit.json', 'w', encoding='utf-8') as f:
        json.dump(js, f, indent=4, ensure_ascii=False)

    with open('twit.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if len(data['users']) == 0:
        return 'This user has no friends'

    map = folium.Map()

    fr_number = 15

    i = 0
    while i <= fr_number <= 99:
        geolocator = Nominatim(user_agent='shos_moe')

        try:
            location = geolocator.geocode(data['users'][i]['location'])
            latitude = location.latitude
            longtitude = location.longitude
            map.add_child(folium.Marker(location=[latitude, longtitude],
                                        popup=data['users'][i]['screen_name'],
                                        icon=folium.Icon()))
        except GeocoderTimedOut as e:
            fr_number += 1
        except AttributeError:
            fr_number += 1
        i += 1
    map.save('templates/Friends.html')
    return 'OK'