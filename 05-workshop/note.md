# Workshop dlt

## install dlt
pip install "dlt[workspace]"


## init project
dlt init dlthub:taxi_pipeline duckdb




## run
python taxi_pipeline.py

```
------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 0.00s | Rate: 0.00/s
Memory usage: 124.67 MB (47.60%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 2.68s | Rate: 0.00/s
nyc_taxi_data: 1000  | Time: 0.00s | Rate: 0.00/s
Memory usage: 127.89 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 5.26s | Rate: 0.00/s
nyc_taxi_data: 2000  | Time: 2.57s | Rate: 777.57/s
Memory usage: 129.52 MB (47.60%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 7.88s | Rate: 0.00/s
nyc_taxi_data: 3000  | Time: 5.20s | Rate: 577.29/s
Memory usage: 131.45 MB (47.60%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 10.32s | Rate: 0.00/s
nyc_taxi_data: 4000  | Time: 7.63s | Rate: 524.01/s
Memory usage: 132.64 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 13.00s | Rate: 0.00/s
nyc_taxi_data: 5000  | Time: 10.31s | Rate: 484.92/s
Memory usage: 133.81 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 15.00s | Rate: 0.00/s
nyc_taxi_data: 6000  | Time: 12.32s | Rate: 487.06/s
Memory usage: 133.95 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 17.01s | Rate: 0.00/s
nyc_taxi_data: 7000  | Time: 14.33s | Rate: 488.49/s
Memory usage: 134.33 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 18.93s | Rate: 0.00/s
nyc_taxi_data: 8000  | Time: 16.24s | Rate: 492.56/s
Memory usage: 134.34 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 21.05s | Rate: 0.00/s
nyc_taxi_data: 9000  | Time: 18.36s | Rate: 490.17/s
Memory usage: 134.34 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 24.18s | Rate: 0.00/s
nyc_taxi_data: 10000  | Time: 21.50s | Rate: 465.11/s
Memory usage: 135.30 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 26.05s | Rate: 0.00/s
nyc_taxi_data: 10000  | Time: 23.37s | Rate: 427.95/s
Memory usage: 135.31 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 1/1 (100.0%) | Time: 26.14s | Rate: 0.04/s
nyc_taxi_data: 10000  | Time: 23.45s | Rate: 426.39/s
Memory usage: 135.48 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 0.00s | Rate: 0.00/s
Memory usage: 135.50 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 0/1 (0.0%) | Time: 0.02s | Rate: 0.00/s
_dlt_pipeline_state: 1  | Time: 0.00s | Rate: 0.00/s
Memory usage: 135.50 MB (47.70%) | CPU usage: 0.00%

------------------------------- Extract rest_api -------------------------------
Resources: 1/1 (100.0%) | Time: 0.05s | Rate: 20.58/s
_dlt_pipeline_state: 1  | Time: 0.03s | Rate: 30.60/s
Memory usage: 135.50 MB (47.70%) | CPU usage: 0.00%

------------------- Normalize rest_api in 1772291804.3177998 -------------------
Files: 0/2 (0.0%) | Time: 0.00s | Rate: 0.00/s
Memory usage: 135.58 MB (47.70%) | CPU usage: 0.00%

------------------- Normalize rest_api in 1772291804.3177998 -------------------
Files: 0/2 (0.0%) | Time: 0.00s | Rate: 0.00/s
Items: 0  | Time: 0.00s | Rate: 0.00/s
Memory usage: 135.58 MB (47.70%) | CPU usage: 0.00%

------------------- Normalize rest_api in 1772291804.3177998 -------------------
Files: 2/2 (100.0%) | Time: 2.25s | Rate: 0.89/s
Items: 0  | Time: 2.25s | Rate: 0.00/s
Memory usage: 135.63 MB (47.70%) | CPU usage: 0.00%

2026-02-28 22:17:13,002|[WARNING]|10556|1664|dlt|validate.py|verify_normalized_table:91|In schema `rest_api`: The following columns in table 'nyc_taxi_data' did not receive any data during this load and therefore could not have their types inferred:
  - rate_code
  - mta_tax

Unless type hints are provided, these columns will not be materialized in the destination.
One way to provide type hints is to use the 'columns' argument in the '@dlt.resource' decorator.  For example:

@dlt.resource(columns={'rate_code': {'data_type': 'text'}})

------------------- Normalize rest_api in 1772291804.3177998 -------------------
Files: 2/2 (100.0%) | Time: 2.28s | Rate: 0.88/s
Items: 10001  | Time: 2.28s | Rate: 4394.27/s
Memory usage: 135.95 MB (47.70%) | CPU usage: 0.00%

--------------------- Load rest_api in 1772291804.3177998 ----------------------
Jobs: 0/2 (0.0%) | Time: 0.00s | Rate: 0.00/s
Memory usage: 145.32 MB (47.70%) | CPU usage: 0.00%

--------------------- Load rest_api in 1772291804.3177998 ----------------------
Jobs: 1/2 (50.0%) | Time: 3.84s | Rate: 0.26/s
Memory usage: 160.13 MB (47.80%) | CPU usage: 0.00%

--------------------- Load rest_api in 1772291804.3177998 ----------------------
Jobs: 2/2 (100.0%) | Time: 4.00s | Rate: 0.50/s
Memory usage: 153.57 MB (47.80%) | CPU usage: 0.00%

Pipeline taxi_pipeline load step completed in 4 seconds
1 load package(s) were loaded to destination duckdb and into dataset taxi_pipeline_dataset_20260228031644
The duckdb destination used duckdb:///C:\srccode\data-engineering-zoomcamp-2026\05-workshop\taxi_pipeline.duckdb location to store data
Load package 1772291804.3177998 is LOADED and contains no failed jobs
```


# run dlt dashboard
```
dlt dashboard
```
- will open in browser http://127.0.0.1:2718/
- select taxi_pipeline
- activate "Dataset Browser: Data and Source/Resource State"
- select data in query


Q1.
```
SELECT
min(trip_pickup_date_time), max(trip_pickup_date_time)
FROM "nyc_taxi_data"
```


Q2.
```
SELECT
  count(payment_type) * 1.0 / (select count(payment_type) from "nyc_taxi_data")
  FROM "nyc_taxi_data" where payment_type='Credit'
```


Q3.
```
SELECT
  sum(tip_amt)
FROM "nyc_taxi_data"
```
  


# Try using marimo
```
pip install marimo "ibis-framework[duckdb]"
```

Try run:
```
marimo edit taxi_pipeline.py
```
Show error:
```
Error: Python script not recognized as a marimo notebook.

  Tip: Try converting with

    marimo convert taxi_pipeline.py -o taxi_pipeline_nb.py

  then open with marimo edit taxi_pipeline_nb.py
```

Convert original py to nb py run:
```
marimo convert taxi_pipeline.py -o taxi_pipeline_nb.py
```

Run again:
```
marimo edit taxi_pipeline.py
```
It's running:
```
        Edit taxi_pipeline_nb.py in your browser 📝

        ➜  URL: http://127.0.0.1:2718?access_token=um0kJNCqZ44KrHQw_5VktA
```











