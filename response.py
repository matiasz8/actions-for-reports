import requests
import json

lat = -34.61315
lon = -58.37723
url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}"
data = requests.post(url)
data = json.loads(data.text)
data = json.dumps(data, indent=2)
# print(data)

# data = {
#     "results": {
#         "sunrise": "10:51:38 AM",
#         "sunset": "9:08:28 PM",
#         "solar_noon": "4:00:03 PM",
#         "day_length": "10:16:50",
#         "civil_twilight_begin": "10:24:46 AM",
#         "civil_twilight_end": "9:35:21 PM",
#         "nautical_twilight_begin": "9:54:12 AM",
#         "nautical_twilight_end": "10:05:54 PM",
#         "astronomical_twilight_begin": "9:24:13 AM",
#         "astronomical_twilight_end": "10:35:53 PM",
#     },
#     "status": "OK",
# }
# data = json.dumps(data)

data = json.loads(data)
print()

for key, val in data["results"].items():
    print(val, key)
