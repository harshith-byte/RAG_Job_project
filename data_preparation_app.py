import pandas as pd
import os

def data_cleaning():
    if os.path.exists('data/cleaned_data.csv'):
        return pd.read_csv('data/cleaned_data.csv')
    df = pd.read_csv('data/jobs_en.csv',on_bad_lines='skip',sep='|')

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    df.to_csv('data/cleaned_data.csv')
    return df