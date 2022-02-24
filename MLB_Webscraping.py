import requests
import json
import pandas as pd

url = "https://bdfed.stitch.mlbinfra.com/bdfed/stats/player?stitch_env=prod&season=2021&sportId=1&stats=season&group=hitting&gameType=R&limit=25&offset=0&sortStat=runsBattedIn&order=desc"

r = requests.get(url)

player_data = r.json()

df = pd.json_normalize(player_data['stats'])
df.to_csv('2021_mlb_data.csv', index=False)
