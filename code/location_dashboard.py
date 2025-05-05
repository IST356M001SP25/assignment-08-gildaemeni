'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")

# Load data
tickets = pd.read_csv("cache/tickets_in_top_locations.csv")
locations = pd.read_csv("cache/top_locations.csv")

# Title and intro
st.title("Top Locations for Parking Tickets within Syracuse")
st.write("This dashboard shows the parking tickets that were issued in the top locations with $1,000 or more in total aggregate violation amounts.")

# User input: dropdown to pick location
location_choice = st.selectbox("Select a location", locations["location"].sort_values())

# Filter tickets for the selected location
subset = tickets[tickets["location"] == location_choice]

# Show totals
c1, c2 = st.columns(2)
c1.metric("Total tickets issued", len(subset))
c2.metric("Total amount", f"${subset['amount'].sum():,.0f}")

# Layout for charts
chart_col1, chart_col2 = st.columns(2)

# Chart 1: Tickets by hour
with chart_col1:
    st.subheader("Tickets Issued by Hour of Day")
    hour_data = subset["hourofday"].value_counts().sort_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=hour_data.index, y=hour_data.values, palette="BuPu", ax=ax1)
    ax1.set_xlabel("Hour")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

# Chart 2: Tickets by day
with chart_col2:
    st.subheader("Tickets Issued by Day of Week")
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_data = subset["dayofweek"].value_counts().reindex(ordered_days)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=day_data.index, y=day_data.values, palette="Spectral", ax=ax2)
    ax2.set_xlabel("Day")
    ax2.set_ylabel("Count")
    st.pyplot(fig2)

# Map section
st.subheader("Map of Selected Location")
if not subset.empty:
    st.map(subset[['lat', 'lon']].dropna().head(1))  # center on 1st result only
else:
    st.warning("No map data for this location.")