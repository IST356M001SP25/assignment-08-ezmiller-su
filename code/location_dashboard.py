'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")

st.title("Top Locations for Parking Within Syracuse")
st.subheader("Dashboard of parking tickets issued in locations totaling at least $1000 in violation fines.")

tickets_in_top_locations = pd.read_csv("cache/tickets_in_top_locations.csv")

top_locations = pd.read_csv("cache/top_locations.csv")['location']
location = st.selectbox("Select a location:", top_locations)

st.text('Total Tickets Issued')
st.subheader(tickets_in_top_locations[tickets_in_top_locations['location'] == location].shape[0])




st.text('Total Amount')
