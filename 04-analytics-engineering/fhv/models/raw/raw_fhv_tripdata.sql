{{ config(materialized='table') }}

SELECT *
FROM read_parquet('data/fhv_tripdata_*.parquet', filename = true)
    