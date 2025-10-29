import pandas as pd

def validate_raw_data(df):
    '''Валидация сырых данных'''
    if df.empty:
        raise ValueError('DataFrame пустой')
    if df.isnull().sum().sum() > 0:
        print('Внимание, пропуски в сырых данных')
    print('Валидация сырых данных выполнена!')

def validate_transformed_data(df):
    '''Валидация преобразованных данных'''
    if df.empty:
        raise ValueError('DataFrame пустой')
    print('Валидация преобразованных данных выполнена!')