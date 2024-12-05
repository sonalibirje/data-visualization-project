import requests

def fetch_air_quality_data(city="Los Angeles"):
    url = "https://api.openaq.org/v2/measurements"
    params = {
        "city": city,
        "parameter": ["pm25", "pm10", "no2", "o3", "so2", "co"],
        "date_from": "2015-01-01",
        "date_to": "2023-12-31",
        "limit": 1000
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    air_quality_data = fetch_air_quality_data()
    print(air_quality_data)
