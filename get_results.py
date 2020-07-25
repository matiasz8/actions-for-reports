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
    paste_data(results)


def get_coor_data(lat, lon) -> Dict[str, Any]:
    try:
        # lon = -58.37723
        url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}"
        data = requests.post(url)
        data = json.loads(data.text)
        data = json.dumps(data, indent=2)
        return data
    except Exception as e:
        print(f"Error: {e}")


def paste_data(coord_data: Dict):
    time_upd = get_time()
    data = ["\n*****", time_upd, "\n", coord_data]
    with open("README.md", "w+") as reader:
        for line in data:
            reader.writelines(line)


def get_time():
    data = datetime.now()
    time = "Last Update: {:%d, %b %Y, %I:%M %p}".format(data)
    return time


if __name__ == "__main__":
    printer()
