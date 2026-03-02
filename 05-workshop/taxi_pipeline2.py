import dlt
import requests

BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
PAGE_SIZE = 1000

@dlt.resource
def nyc_taxi_data():
    page = 0
    while True:
        url = f"{BASE_URL}?page={page}"
        response = requests.get(url)
        data = response.json()
        if not data:
            break
        yield data
        page += 1

@dlt.pipeline(name="taxi_pipeline2")
def taxi_pipeline2():
    return nyc_taxi_data()
