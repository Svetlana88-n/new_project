import pandas as pd

def read_dataset(url):
    df=pd.read_csv(url)
    print(df.head(10))
    return df

url = 'https://drive.google.com/uc?id=1C_iqgpDk2RqQJzV_5J2Nok8DfFMomVbQ'
df = read_dataset(url)

print("Original Data Types:")
print(df.dtypes)

newdf = df.convert_dtypes()

print(" \nNew Data Types:")
print(newdf.dtypes)

df.to_parquet('data.parquet', index=False)
print("Data save in data.parquet")
