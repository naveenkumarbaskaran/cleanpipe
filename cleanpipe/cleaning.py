import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler

def drop_missing(df, axis=0):
    """Drop rows (axis=0) or columns (axis=1) with missing values."""
    return df.dropna(axis=axis)

def fill_missing(df, value, columns=None):
    """Fill missing values with a specified value.
    
    If columns are specified, fill only those columns; otherwise, fill the entire DataFrame.
    """
    if columns:
        df[columns] = df[columns].fillna(value)
    else:
        df = df.fillna(value)
    return df

def convert_dtype(df, column, dtype):
    """Convert the datatype of a column."""
    df[column] = df[column].astype(dtype)
    return df

def rename_columns(df, mapping):
    """Rename columns using a dictionary mapping."""
    return df.rename(columns=mapping)

def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()

def remove_outliers(df, columns, threshold=1.5):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df

def standardize_date_format(df, column, date_format='%Y-%m-%d'):
    """Convert date column to a standard format."""
    df[column] = pd.to_datetime(df[column]).dt.strftime(date_format)
    return df

def encode_categorical(df, columns):
    """One-hot encode specified categorical columns."""
    return pd.get_dummies(df, columns=columns)

def scale_features(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def impute_missing(df, strategy='mean', columns=None):
    """Impute missing values using specified strategy."""
    if columns is None:
        columns = df.columns
    for col in columns:
        if strategy == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == 'median':
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == 'mode':
            df[col].fillna(df[col].mode()[0], inplace=True)
    return df

class CleanPipe:
    def __init__(self, df):
        self.df = df.copy()

    def drop_missing(self, axis=0):
        self.df = self.df.dropna(axis=axis)
        return self

    def fill_missing(self, value, columns=None):
        if columns:
            self.df[columns] = self.df[columns].fillna(value)
        else:
            self.df = self.df.fillna(value)
        return self

    def convert_dtype(self, column, dtype):
        self.df[column] = self.df[column].astype(dtype)
        return self

    def rename_columns(self, mapping):
        self.df = self.df.rename(columns=mapping)
        return self

    def get_df(self):
        return self.df
