import pandas as pd

def read_dataset(url):
    df=pd.read_csv(url)
    print(df.head(10))
    return df

url = 'https://drive.google.com/uc?id=1C_iqgpDk2RqQJzV_5J2Nok8DfFMomVbQ'
df = read_dataset(url)

