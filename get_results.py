import click
from typing import Dict, Any
import json
import requests
from datetime import timezone, datetime, timedelta


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


def paste_data(coord_data, lat, lon):
    time_upd = get_time()
    print(f"Coord: {coord_data}")
    print(f"Lat: {lat}")
    print(f"Lat: {lon}")
    print(coord_data)
    with open("README.md", "w+") as reader:
        
        reader.write(f"{get_badged()} \n\n")
        reader.write(f"\n## *****{time_upd}*****\n\n")
        reader.write(f"\n\n\t\t Latitud: {lat}\n\t\t Longitud: {lon}\n\n")
        for key, val in coord_data["results"].items():
            reader.write(f" - {key} \t {val}\n")

def get_badged():
    return ![report action](https://github.com/matiasz8/actions-for-reports/workflows/report%20action/badge.svg?branch=develop)

def get_time():
    time = datetime.now()
    timezone_hs = -3
    d = datetime(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second,
        tzinfo=timezone(timedelta(hours=timezone_hs)),
    )

    time = d.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    data = f"Last update {time}"
    return data


if __name__ == "__main__":
    printer()
