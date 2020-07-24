import requests
import json

lat = -34.61315
lon = -58.37723
url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}"
data = requests.post(url)
data = json.loads(data.text)
data = json.dumps(data, indent=2)
print(data)

