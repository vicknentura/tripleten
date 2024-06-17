import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('vehicles_us.csv')

st.title("Nico's Used Car App", divider='blue')
st.header('Vehicles in the U.S. from 1955 to 2019')
st.divider()

# Create a checkbox to toggle the histogram
show_odometer = st.checkbox("I'm interested in data on odometer readings")
show_model_year = st.checkbox("I'm interested in the distribution of model years")
show_price_odometer = st.checkbox("I'm interested in the relationship between price and odometer reading")

if show_odometer:
    # Create a histogram of odometer readings
    fig = px.histogram(vehicles_us, x="odometer", nbins=10)
    st.write("Histogram of Odometer Readings")
    st.plotly_chart(fig)
else:
    st.write("No histogram to display")

if show_model_year:
     # Create a histogram of odometer readings
     fig = px.histogram(vehicles_us, x="model_year", nbins=15)
     st.write("Histogram of Model Year")
     st.plotly_chart(fig)
else:
     st.write("No histogram to display")

if show_price_odometer:
     # Create a scatter plot of price vs odometer
     fig = px.scatter(vehicles_us, x="odometer", y="price")
     st.write("Scatter Plot of Price vs Odometer")
     st.plotly_chart(fig)
else:
     st.write("No scatterplot to display")
