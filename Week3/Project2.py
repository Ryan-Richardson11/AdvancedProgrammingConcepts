import requests

def get_destination(latitude, longitude):

    url = f"https://api.weather.gov/points/{latitude},{longitude}"

    response = requests.get(url)
    print(response.json())
    if response.ok:
        office = response.json()['properties']['periods'][0]['officeId']
        gridX = response.json()['properties']['periods'][0]['gridX']
        gridY = response.json()['properties']['periods'][0]['gridY']
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


location = get_destination(37.7749, -122.4194)
forcast = get_forecast(location[0], location[1], location[2])
print(forcast)
