import requests
import json
from datetime import timezone, datetime, timedelta


def get_data():
    lat = -34.61315
    lon = -58.37723
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}"
    data = requests.post(url)
    data = json.loads(data.text)
    data = json.dumps(data, indent=2)
    print(data)


def force_data():

    data = {
        "results": {
            "sunrise": "10:51:38 AM",
            "sunset": "9:08:28 PM",
            "solar_noon": "4:00:03 PM",
            "day_length": "10:16:50",
            "civil_twilight_begin": "10:24:46 AM",
            "civil_twilight_end": "9:35:21 PM",
            "nautical_twilight_begin": "9:54:12 AM",
            "nautical_twilight_end": "10:05:54 PM",
            "astronomical_twilight_begin": "9:24:13 AM",
            "astronomical_twilight_end": "10:35:53 PM",
        },
        "status": "OK",
    }
    data = json.dumps(data)

    data = json.loads(data)

    for key, val in data["results"].items():
        print(val, key)


time = datetime.now()

d = datetime(
    time.year,
    time.month,
    time.day,
    time.hour,
    time.minute,
    time.second,
    tzinfo=timezone(timedelta(hours=0)),
)

# time = d.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
time = d.astimezone(timezone.utc).strftime("%d-%m-%Y %H:%M:%S")
print(time)
