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



st.text('Total Tickets Issued')
st.metric(tickets_in_top_locations[tickets_in_top_locations['location'] == location].shape[0])

st.text('Total Amount')
st.metric("Total amount", f"$ {top_locations['amount'].sum()}")