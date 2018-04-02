# from requests import get
import requests
import html

r = requests.get('http://api.icndb.com/jokes/155')

response = r.json()

strng = 'Joke ID: {}\nJoke: {}'.format(
                                        response['value']['id'],
                                        response['value']['joke']
                                        )

print(html.unescape(strng))
