import requests
import pandas as pd

def convert_to_df_and_save(
    data: list[dict],
    fname: str,
) -> pd.DataFrame | None:
    if data:
        df = pd.DataFrame(data)
        df.to_csv(fname, index=False)
        return df

    return None

url = "https://api.thecatapi.com/v1"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "live_6YSPIu57eJ8nspEUlLR3P8Uz4N1LZheqLt9sPI4DSGkEWu6ObGj176y7hUCA8uR7"
}

response = requests.get(url + "/images/search?limit=10")
print(response)
data = response.json()
print(data)
df = pd.DataFrame(data)

print(df.info())
print(df.head(10))
print(f"Количество изображений: {len(df)}")
print(f"Колонки: {list(df.columns)}")
print(f"Размеры изображений: {df['width'].min()}x{df['height'].min()} - {df['width'].max()}x{df['height'].max()}")

result = convert_to_df_and_save(data, "cat_images.csv")
print(result.info())
