import marimo

__generated_with = "0.20.2"
app = marimo.App()


@app.cell
def _():
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

    def _main_():
        load_info = pipeline.run(nyc_taxi_api_source())
        print(load_info)

    _main_()
    return


@app.cell
def _():
    import marimo as mo
    import duckdb

    return duckdb, mo


@app.cell
def _(duckdb):
    # query using con in regular cell
    con = duckdb.connect("taxi_pipeline.duckdb")

    con.sql("SELECT * FROM taxi_pipeline_dataset_20260301105150.nyc_taxi_data LIMIT 10").show()
    return (con,)


@app.cell
def _(con, mo):
    _df = mo.sql(
        f"""
        -- cell type sql, write query directy, but choose db connection first (con)
        SELECT * FROM taxi_pipeline_dataset_20260301105150.nyc_taxi_data LIMIT 10
        """,
        engine=con
    )
    return


if __name__ == "__main__":
    app.run()
