import pandas as pd
import os


def extract(url):
    df = pd.read_csv(url)

    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/raw_data.csv', index=False)
    print("Сырые данные сохранены в data/raw/raw_data.csv")
    return df