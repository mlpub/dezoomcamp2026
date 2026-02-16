dbt build
09:29:20  Running with dbt=1.11.3
09:29:21  Registered adapter: duckdb=1.10.0
09:29:21  Found 2 models, 472 macros
09:29:21
09:29:21  Concurrency: 1 threads (target='dev')
09:29:21
09:29:22  1 of 2 START sql table model dev.raw_fhv_tripdata .............................. [RUN]
09:29:45  1 of 2 OK created sql table model dev.raw_fhv_tripdata ......................... [OK in 23.14s]
09:29:45  2 of 2 START sql view model dev.stg_fhv_tripdata ............................... [RUN]
09:29:45  2 of 2 OK created sql view model dev.stg_fhv_tripdata .......................... [OK in 0.06s]
09:29:45
09:29:45  Finished running 1 table model, 1 view model in 0 hours 0 minutes and 23.45 seconds (23.45s).
09:29:45
09:29:45  Completed successfully
09:29:45
09:29:45  Done. PASS=2 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=2