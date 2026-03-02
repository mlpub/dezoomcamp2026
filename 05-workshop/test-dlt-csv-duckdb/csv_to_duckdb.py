import csv
from pathlib import Path

import dlt


CSV_PATH = Path(r"D:\\data\\3a-superstore\\Customers_ENG.csv")


def read_customers_csv():
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            yield row


if __name__ == "__main__":
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")

    pipeline = dlt.pipeline(
        pipeline_name="superstore_csv_pipeline",
        destination="duckdb",
        dataset_name="superstore_data",
        dev_mode=True,
        progress="log",
    )
    load_info = pipeline.run(
        read_customers_csv(),
        table_name="customers_eng",
        write_disposition="replace",
    )
    print(load_info)
