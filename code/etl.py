import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    amount_per_location_df = violations_df.pivot_table(index='location', values='amount', aggfunc='sum').sort_values(by='amount')
    amount_per_location_df['location'] = amount_per_location_df.index
    amount_per_location_df.reset_index(drop=True, inplace=True)
    amount_per_location_df = amount_per_location_df[amount_per_location_df['amount'] >= threshold]
    return amount_per_location_df


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locations_df = top_locations(violations_df, threshold)
    violation_locations_df = violations_df[['location', 'lat', 'lon']].drop_duplicates(subset=['location'])
    merged_df = pd.merge(top_locations_df, violation_locations_df, on='location')
    return merged_df


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    return pd.DataFrame()  # TODO implement this function

if __name__ == '__main__':
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    top_locations_df = top_locations(violations_df)
    top_locations_df.to_csv('./cache/top_locations.csv', index=False)
    merged_df = top_locations_mappable(violations_df)
    merged_df.to_csv('./cache/top_locations_mappable.csv', index=False)