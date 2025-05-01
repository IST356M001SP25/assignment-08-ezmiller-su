'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")


tickets_in_top_locations = pd.read_csv("cache/tickets_in_top_locations.csv")


st.title("Top Locations for Parking Within Syracuse")
st.subheader("Dashboard of parking tickets issued in locations totaling at least $1000 in violation fines.")

locations = tickets_in_top_locations['location'].unique()

location = st.selectbox("Select a location:", locations)

selected_location = tickets_in_top_locations[tickets_in_top_locations['location'] == location]


st.metric("Total tickets issued", selected_location.shape[0])

st.metric("Total amount", f"$ {selected_location['amount'].sum()}")