import requests
import json
OWM_KEY = 'c6311d9ec7ce3538db5dfefb668ed619'

class WeatherStation:
    def __init__(self, key):
        self.url = 'https://api.openweathermap.org/data/2.5/weather'
        self.auth_key = key

    def connect(self, **kwargs):
        package = {
                "APPID": self.auth_key,
                "units": "imperial"
            }
        package.update(kwargs)
        return requests.post('https://api.openweathermap.org/data/2.5/weather', params=package)

    def get_city_temp(self, city):
        # q = input('What city would you like to check?: ')
        response = self.connect(q=city)
        return 'The weather in {} is {}.'.format(q.title(), response.json()['main']['temp'])

    def get_coords_temp(self):
        # lat={lat}&lon={lon}
        lat = input('What is the lat?: ')
        lon = input('What is the lon?: ')
        response = self.connect(lat=lat, lon=lon)
        return 'The weather in {} is {}.'.format(response.json()['name'], response.json()['main']['temp'])


if __name__ == '__main__':
        station = WeatherStation(OWM_KEY)
        print(station.get_coords_temp())
