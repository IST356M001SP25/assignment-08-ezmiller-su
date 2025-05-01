import pandas as pd
import streamlit as st 

def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    violations_df = violations_df[['location', 'amount']][violations_df['amount'] > 1000]
    return violations_df


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    violations_df = violations_df[['location', 'lat', 'lon', 'amount']][violations_df['amount'] > 1000]
    return pd.DataFrame(violations_df)


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    return pd.DataFrame()  # TODO implement this function

if __name__ == '__main__':
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    top_locations_df = top_locations(violations_df)
    print(top_locations_df)
