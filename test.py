import googlemaps
from datetime import datetime
import csv
import time


def get_data(start, end, gmaps, file):
    now = datetime.now()
    directions_result = gmaps.directions(start,
                                         end,
                                         mode="driving",
                                         departure_time=now)

    print(len(directions_result))
    for item in directions_result:
        print(item['summary'])
        legs = item['legs']
        for leg in legs:
            print(leg['duration_in_traffic'])
            print(leg['distance'])
            print(leg['duration'])
            c=open(file, 'a')
            writer = csv.writer(c)
            writer.writerow([time.time(), item['summary'], leg['distance']['value'], leg['duration_in_traffic']['value'], leg['duration']['value'], now])
            c.close()


gmaps = googlemaps.Client(key='AIzaSyA5EkTQrTRaiwxOExL6yIt8P43x6kU2d7U')

# Request directions via public transit

get_data(home, work, gmaps, 'h2w.csv')
get_data(work, home, gmaps, 'w2h.csv')
