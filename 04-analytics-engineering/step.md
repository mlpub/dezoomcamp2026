
# setup dbt


# install duckdb
Python:
```
pip install duckdb
```
CLI:
```
# linux
curl https://install.duckdb.org | sh

# windows
https://install.duckdb.org/v1.4.4/duckdb_cli-windows-amd64.zip
```


# Download ingest data


# Test dbt connection
```
dbt debug
```
Result:
```
dbt debug
01:01:41  Running with dbt=1.11.3
01:01:42  dbt version: 1.11.3
01:01:42  python version: 3.10.12
01:01:42  python path: /home/demo/venv/ml2/bin/python3
01:01:42  os info: Linux-6.8.0-94-generic-x86_64-with-glibc2.35
01:01:42  Using profiles dir at /home/demo/.dbt
01:01:42  Using profiles.yml file at /home/demo/.dbt/profiles.yml
01:01:42  Using dbt_project.yml file at /home/demo/srccode/learnmachinelearning/data-engineering-zoomcamp-2026/04-analytics-engineering/hw4/taxi_rides_ny/dbt_project.yml
01:01:42  adapter type: duckdb
01:01:42  adapter version: 1.10.0
01:01:42  Configuration:
01:01:42    profiles.yml file [OK found and valid]
01:01:42    dbt_project.yml file [OK found and valid]
01:01:42  Required dependencies:
01:01:42   - git [OK found]

01:01:42  Connection:
01:01:42    database: taxi_rides_ny
01:01:42    schema: dev
01:01:42    path: taxi_rides_ny.duckdb
01:01:42    config_options: None
01:01:42    extensions: ['parquet']
01:01:42    settings: {'memory_limit': '2GB', 'preserve_insertion_order': False}
01:01:42    external_root: .
01:01:42    use_credential_provider: None
01:01:42    attach: None
01:01:42    filesystems: None
01:01:42    remote: None
01:01:42    plugins: None
01:01:42    disable_transactions: False
01:01:42  Registered adapter: duckdb=1.10.0
01:01:42    Connection test: [OK connection ok]

01:01:42  All checks passed!
```


# Check duckdb data
```
duckdb taxi_rides_ny.duckdb
```

## release duckdb accidentally press ctrl+z
i run duckdb data.duckdb from terminal and i exit by press ctrl+z (back to shell). when run `duckdb data.duckdb` again it show message "IO Error: Could not set lock on file". how to release it?

Solution:
1. check duckdb process
```
ps -Af|grep duckdb
demo    33251    3667  0 08:21 pts/0    00:00:00 duckdb taxi_rides_ny.duckdb
```
1. from terminal press `fg`. It will back to duckdb and than enter `.exit` or press ctrl+d.
2. Get the process id and kill.
```
ps -Af|grep duck
demo    33768    3667  0 08:22 pts/0    00:00:00 duckdb taxi_rides_ny.duckdb

kill -9 33768
```

# Explore data in duckdb
1. Show tables
```
.tables
green_tripdata   yellow_tripdata
```

2. Count a table
```
select count(*) from prod.green_tripdate
┌────────────────┐
│  count_star()  │
│     int64      │
├────────────────┤
│    7778101     │
│ (7.78 million) │
└────────────────┘
```
Remember to put schema `prod`, if it missing, it will show error:
```
Catalog Error:
Table with name green_tripdata does not exist!
Did you mean "prod.green_tripdata"?

LINE 1: select count(*) from green_tripdata;
```

3. Select data
```
select * from prod.green_tripdata limit 10;
┌──────────┬──────────────────────┬───┬───────────┬──────────────────────┐
│ VendorID │ lpep_pickup_datetime │ … │ trip_type │ congestion_surcharge │
│  int64   │      timestamp       │   │   int64   │       varchar        │
├──────────┼──────────────────────┼───┼───────────┼──────────────────────┤
│        2 │ 2018-12-21 15:17:29  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:10:16  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:27:11  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:46:20  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:19:06  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:12:35  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:47:55  │ … │         1 │ NULL                 │
│        1 │ 2019-01-01 00:12:47  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:16:23  │ … │         1 │ NULL                 │
│        2 │ 2019-01-01 00:58:02  │ … │         1 │ NULL                 │
├──────────┴──────────────────────┴───┴───────────┴──────────────────────┤
│ 10 rows                                           20 columns (4 shown) │
└────────────────────────────────────────────────────────────────────────┘
```

4. Get table structure
```
describe prod.green_tripdata;

┌───────────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│      column_name      │ column_type │  null   │   key   │ default │  extra  │
│        varchar        │   varchar   │ varchar │ varchar │ varchar │ varchar │
├───────────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ VendorID              │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ lpep_pickup_datetime  │ TIMESTAMP   │ YES     │ NULL    │ NULL    │ NULL    │
│ lpep_dropoff_datetime │ TIMESTAMP   │ YES     │ NULL    │ NULL    │ NULL    │
│ store_and_fwd_flag    │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ RatecodeID            │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ PULocationID          │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ DOLocationID          │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ passenger_count       │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ trip_distance         │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ fare_amount           │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ extra                 │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ mta_tax               │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ tip_amount            │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ tolls_amount          │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ ehail_fee             │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ improvement_surcharge │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ total_amount          │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ payment_type          │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ trip_type             │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ congestion_surcharge  │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
├───────────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┤
│ 20 rows                                                           6 columns │
└─────────────────────────────────────────────────────────────────────────────┘
```

For table detail:
```
summarize prod.green_tripdata;

┌──────────────────────┬─────────────┬───┬─────────┬─────────────────┐
│     column_name      │ column_type │ … │  count  │ null_percentage │
│       varchar        │   varchar   │   │  int64  │  decimal(9,2)   │
├──────────────────────┼─────────────┼───┼─────────┼─────────────────┤
│ VendorID             │ BIGINT      │ … │ 7778101 │           12.11 │
│ lpep_pickup_datetime │ TIMESTAMP   │ … │ 7778101 │            0.00 │
│ lpep_dropoff_datet…  │ TIMESTAMP   │ … │ 7778101 │            0.00 │
│ store_and_fwd_flag   │ VARCHAR     │ … │ 7778101 │           12.11 │
│ RatecodeID           │ BIGINT      │ … │ 7778101 │           12.11 │
│ PULocationID         │ BIGINT      │ … │ 7778101 │            0.00 │
│ DOLocationID         │ BIGINT      │ … │ 7778101 │            0.00 │
│ passenger_count      │ BIGINT      │ … │ 7778101 │           12.11 │
│ trip_distance        │ DOUBLE      │ … │ 7778101 │            0.00 │
│ fare_amount          │ DOUBLE      │ … │ 7778101 │            0.00 │
│ extra                │ DOUBLE      │ … │ 7778101 │            0.00 │
│ mta_tax              │ DOUBLE      │ … │ 7778101 │            0.00 │
│ tip_amount           │ DOUBLE      │ … │ 7778101 │            0.00 │
│ tolls_amount         │ DOUBLE      │ … │ 7778101 │            0.00 │
│ ehail_fee            │ VARCHAR     │ … │ 7778101 │          100.00 │
│ improvement_surcha…  │ DOUBLE      │ … │ 7778101 │            0.00 │
│ total_amount         │ DOUBLE      │ … │ 7778101 │            0.00 │
│ payment_type         │ BIGINT      │ … │ 7778101 │           12.11 │
│ trip_type            │ BIGINT      │ … │ 7778101 │           12.12 │
│ congestion_surcharge │ VARCHAR     │ … │ 7778101 │           19.14 │
├──────────────────────┴─────────────┴───┴─────────┴─────────────────┤
│ 20 rows                                       12 columns (4 shown) │
└────────────────────────────────────────────────────────────────────┘
```




# Using dbt from scratch
## Init dbt using duckdb
```
dbt init demo_project

01:56:01  Running with dbt=1.11.3
01:56:01  
Your new dbt project "demo_project" was created!

For more information on how to configure the profiles.yml file,
please consult the dbt documentation here:

  https://docs.getdbt.com/docs/configure-your-profile

One more thing:

Need help? Don't hesitate to reach out to us via GitHub issues or on Slack:

  https://community.getdbt.com/

Happy modeling!

01:56:01  Setting up your profile.
Which database would you like to use?
[1] duckdb

(Don't see the one you want? https://docs.getdbt.com/docs/available-adapters)

Enter a number: 1

```















