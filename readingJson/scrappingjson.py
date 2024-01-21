import requests

def scrappingJson():
    r1 = requests.get('https://data.covid19india.org/v4/min/data.min.json')
    r2 = requests.get('https://data.covid19india.org/v4/min/timeseries.min.json')
    if r1.status_code == 200 and r2.status_code == 200:
        json_data_One = r1.json()
        json_data_Two = r2.json()
        return json_data_One,json_data_Two