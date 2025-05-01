'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd
# these constants should help you get the map to look better
# you need to figure out where to use them
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale

mapdata = pd.DataFrame(pd.read_csv('cache/top_locations_mappable.csv'))

st.title('Syracuse: Most Frequent Areas for Parking Tickets')

geo_df = gpd.GeoDataFrame(mapdata, geometry=gpd.points_from_xy(mapdata.lon, mapdata.lat))

emptymap = folium.Map(location=CUSE, zoom_start=ZOOM)

map = geo_df.explore(geo_df['amount'], m=emptymap, 
                       cmap="plasma",vmin=VMIN, vmax=VMAX, 
                       legend=True, legend_name='Amount',
                       marker_type = "circle",
                       marker_kwds = {"radius": 40, "fill": True})

sf.folium_static(map)