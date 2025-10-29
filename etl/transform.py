import pandas as pd

def transform(df):
    newdf = df.convert_dtypes()
    print("Типы данных преобразованы")
    return newdf