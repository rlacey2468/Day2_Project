import requests

url = 'https://developer.twitter.com/en/docs/twitter-api'

response = requests.get(url)

if response.status_code == 200:
  print (response.json())