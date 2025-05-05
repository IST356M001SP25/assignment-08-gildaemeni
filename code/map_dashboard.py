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

# Title and brief intro
st.title("Top Locations for Parking Tickets within Syracuse")
st.write("This dashboard shows the parking tickets that were issued in the top locations with $1,000 or more in total aggregate violation amounts.")

# Load data
df = pd.read_csv("cache/top_locations_mappable.csv")

# Set up base folium map
base_map = folium.Map(location=CUSE, zoom_start=ZOOM)

# Define a linear color scale
from branca.colormap import linear
color_scale = linear.YlOrRd_09.scale(VMIN, VMAX)
color_scale.caption = "Fine Amount ($)"
color_scale.add_to(base_map)

# Plot circles on the map
for _, row in df.iterrows():
    folium.CircleMarker(
        location=(row["lat"], row["lon"]),
        radius=row["amount"] / 500,  # adjust for visibility
        popup=f"{row['location']} — ${row['amount']:.2f}",
        color=color_scale(row["amount"]),
        fill=True,
        fill_opacity=0.6
    ).add_to(base_map)

# Render the map in Streamlit
sf.folium_static(base_map)