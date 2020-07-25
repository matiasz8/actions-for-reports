import click
from typing import Dict, Any
import json
import requests
from datetime import datetime


@click.command()
@click.option("--lat", help="Latitud value")
@click.option("--lon", help="Longitud value")
def printer(lat, lon):

    results = get_coor_data(lat, lon)
    click.echo(f"lat: {lat}")
    click.echo(f"long: {lon}")
    paste_data(results, lat, lon)


def get_coor_data(lat, lon) -> Dict[str, Any]:
    try:
        url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}"
        data = requests.post(url)
        data = json.loads(data.text)
        # data = json.dumps(data, indent=2)
        return data
    except Exception as e:
        print(f"Error: {e}")


def paste_data(coord_data: Dict, lat, lon):
    time_upd = get_time()
    with open("README.md", "w+") as reader:
        reader.write(f"\n## *****{time_upd}*****\n\n")
        reader.write(f"\n\n\t\t### Latitud: {lat}\n\t\t### Longitud: {lon}\n\n")
        for key, val in coord_data["results"].items():
            reader.write(f" - {key} \t {val}\n")


def get_time():
    data = datetime.now()
    time = "Last Update: {:%d, %b %Y, %I:%M %p}".format(data)
    return time


if __name__ == "__main__":
    printer()
