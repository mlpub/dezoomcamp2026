import pandas as pd
import pyarrow.parquet as pq
from tqdm.auto import tqdm
from sqlalchemy import create_engine
import click


data1 = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
data2 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'



def ingest_data1(user, password, host, port, db, table):
    df = pd.read_parquet(data1, engine="pyarrow")

    # Create Database Connection
    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db}'
    )

    chunksize = 50_000

    first = True

    for start in range(0, len(df), chunksize):
        df_chunk = df.iloc[start:start + chunksize]

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name="green_tripdata",
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        df_chunk.to_sql(
            name="green_tripdata",
            con=engine,
            if_exists="append",
        )







def ingest_data2(user, password, host, port, db, table):
    # Ingestion logic here
    # Read a sample of the data
    dtype = {
        "LocationID": "Int64",
        "Borough": "string",
        "Zone": "string",
        "service_zone": "string"
    }


    # Create Database Connection
    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db}'
    )

    df_iter = pd.read_csv(
        data2,
        dtype=dtype,
        iterator=True,
        chunksize=100000
    )

    first = True

    for df_chunk in tqdm(df_iter):

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name="taxi_zone_lookup",
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        # Insert chunk
        df_chunk.to_sql(
            name="taxi_zone_lookup",
            con=engine,
            if_exists="append"
        )

        print("Inserted:", len(df_chunk))


@click.command()
@click.option('--user', default='postgres', help='PostgreSQL user')
@click.option('--password', default='postgres', help='PostgreSQL password')
@click.option('--host', default='db', help='PostgreSQL host')
@click.option('--port', default=5432, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='green_tripdata', help='Target table name')
def ingest_data(user, password, host, port, db, table):
    ingest_data1(user, password, host, port, db, table)
    ingest_data2(user, password, host, port, db, table)



if __name__ == "__main__":
    ingest_data()

