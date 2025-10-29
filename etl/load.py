import sqlite3
import pandas as pd
import os
from sqlalchemy import create_engine, text


def get_postgres_creds():
    conn = sqlite3.connect('creds.db')
    cursor = conn.cursor()
    cursor.execute("SELECT url, port, user, pass FROM access")
    url, port, user, password = cursor.fetchone()
    conn.close()
    return url, port, user, password


def load_to_db(df, limit=100):
    url, port, user, password = get_postgres_creds()

    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks")

    data = df.head(limit)

    data.to_sql(
        name="kalaturskaya",
        con=engine,
        schema="public",
        if_exists="replace",
        index=False,
    )
    os.makedirs('data/processed', exist_ok=True)
    data.to_parquet('data/processed/processed_data.parquet', index=False)

    with engine.begin() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM public.kalaturskaya"))
        print(f"DB rows: {result.fetchone()[0]}")