import requests

package = {
    'APPID': 'c6311d9ec7ce3538db5dfefb668ed619',
    'q': 'portland'
}

r = requests.post('https://api.openweathermap.org/data/2.5/weather', params=package)

print(r.json())
