import requests
import json
from pyyoutube import Api


API_KEY= "AIzaSyAr57EoQGSk5pW7WnpxblC0Q_7xcHtKXNw"
#not sure if necessary
api = Api(api_key="AIzaSyAr57EoQGSk5pW7WnpxblC0Q_7xcHtKXNw")

url='https://www.googleapis.com/youtube/v3/videos'

parameters = {
  'key': API_KEY,
  'part':'snippet',
  'chart':'mostPopular',
  'maxResults' : 3,
}

response=requests.get(url, params=parameters)

if response.status_code == 200:
  data = response.json()
  for item in data.get('items', []):
        video_id = item['id']
        title = item['snippet']['title']
        description = item['snippet']['description']
        
        print(f"Video ID: {video_id}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print("\n")
else:
  print(response.status_code)



