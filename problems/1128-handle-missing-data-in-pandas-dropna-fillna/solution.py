import pandas as pd

def solution(df):
    df = df.loc[:, df.isna().mean(axis = 0) <= 0.5]
    df = df.loc[df.isna().mean(axis = 1) <= 0.5, :]

    for i in range(df.shape[1]):
        if pd.api.types.is_numeric_dtype(df.iloc[:,i]):
            df.iloc[:,i] = (df.iloc[:,i]).fillna(df.iloc[:,i].mean())
        else:
            df.iloc[:,i] = (df.iloc[:,i]).fillna(df.iloc[:,i].mode().iloc[0])

    df.reset_index(drop = True)

    return df