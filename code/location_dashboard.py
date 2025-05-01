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
fig1, ax1 = plt.subplots()
ax1.set_title('Tickets Issued by Hour of Day')
sns.barplot(data=selected_location, x="hourofday", y="count", estimator="sum", hue="hourofday", ax=ax1)
st.pyplot(fig1)

st.metric("Total amount", f"$ {selected_location['amount'].sum()}")
fig2, ax2 = plt.subplots()
ax2.set_title('Tickets Issued by Day of Week')
sns.barplot(data=selected_location, x="dayofweek", y="count", estimator="sum", hue="dayofweek", ax=ax2)
st.pyplot(fig2)

st.map(selected_location[['lat', 'lon']])