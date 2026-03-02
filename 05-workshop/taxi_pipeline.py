import dlt
from dlt.sources.rest_api import rest_api_source
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def nyc_taxi_api_source():
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/",
            "paginator": {
                "type": "page_number",
                "base_page": 1,
                "page_param": "page",
                "total_path": None,
            },
        },
        "resources": [
            {
                "name": "nyc_taxi_data",
                "endpoint": {
                    "path": "data_engineering_zoomcamp_api",
                },
            }
        ],
    }

    return rest_api_source(config)


pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    progress="log",
    dev_mode=True,
)


if __name__ == "__main__":
    load_info = pipeline.run(nyc_taxi_api_source())
    print(load_info)
