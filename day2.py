import requests
import json
import pandas as pd
import sqlalchemy as db
from pyyoutube import Api


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
        #description = item['snippet']['description']
        
        print(f"Video ID: {video_id}")
        print(f"Title: {title}")
        #print(f"Description: {description}")
        print("\n")
else:
  print(response.status_code)

video_data = []
for item in data.get('items', []):
    video_data.append({
        'video_id': item['id'],
        'title': item['snippet']['title'],
        'published_at': item['snippet']['publishedAt'],
        'channel_title': item['snippet']['channelTitle']
        # Add more fields as needed
    })
print(video_data)

data_base = pd.DataFrame.from_dict(video_data)
engine = db.create_engine('sqlite:///data_base.db')

data_base.to_sql('videos', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))
