import requests

def get_destination():
    latitude = float(input("Enter the locations latitude: "))
    if latitude < -90 or latitude > 90:
        print("Invalid. Latitude must be between -90 and 90")

    longitude = float(input("Enter the locations longitude: "))
    if longitude < -180 or longitude > 180:
        print("Invalid. Longitude must be between -180 and 180")

    url = f"https://api.weather.gov/points/{latitude},{longitude}"

    response = requests.get(url)

    if response.ok:
        office = response.json()['properties']['cwa']
        gridX = response.json()['properties']['gridX']
        gridY = response.json()['properties']['gridY']
        return (office, gridX, gridY)
    else:
        raise Exception('Failed to fetch location.')

def get_forecast(office, gridX, gridY):
    # Construct the API URL for the given latitude and longitude
    url = f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast'

    # Send a GET request to the API URL
    response = requests.get(url)
    # If the response is successful, extract the forecast data
    if response.ok:
        forecast = str(response.json()['properties']
                       ['periods'][0]['temperature'])
        forecast += "F " + \
            str(response.json()['properties']
                ['periods'][0]['temperatureTrend'])
        forecast += " - " + \
            str(response.json()['properties']['periods'][0]['shortForecast'])
        return forecast

    # If the response is not successful, raise an exception
    else:
        raise Exception('Failed to fetch forecast.')


try:
    location = get_destination()
    forecast = get_forecast(location[0], location[1], location[2])
    print(forecast)
except Exception as e:
    print(f"Error: {e}")
