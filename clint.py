import requests
import pandas as pd

df = pd.read_csv('test.csv')

print(df)

dff = df.to_json()
url = 'http://localhost:8085/api'

r = requests.post(url , data=dff)



