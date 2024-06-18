import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('vehicles_us.csv')

st.title("Used Car Insights Generator")
st.header(":red[Vehicles in the U.S. from 1955 to 2019] :blue_car:")
st.divider()

st.header("Data Exploration")
st.subheader("Well, let me poke around then!")

# Create a checkbox to toggle the histogram
show_odometer = st.checkbox("I'm interested in data on odometer readings")
show_model_year = st.checkbox("I'm interested in the distribution of model years")
show_price_odometer = st.checkbox("I'm interested in the relationship between price and odometer reading")

if show_odometer:
    # Create a histogram of odometer readings
    fig = px.histogram(vehicles_us, x="odometer", nbins=10)
    st.write("Histogram of Odometer Readings")
    st.plotly_chart(fig)
    print("It looks like nearly all cars sold are around or below 200K miles driven. See stats section below.")
else:
    st.write("Click the checkbox for viz and insights")

if show_model_year:
    # Create a histogram of model_year
    fig = px.histogram(vehicles_us, x="model_year", nbins=15)
    st.write("Histogram of Model Year")
    st.plotly_chart(fig)
    print("Interesting, we can see that nearly all cars that are listed on this website are from recent years – specifically, the last two decades.")
else:
    st.write("Click the checkbox for viz and insights")

if show_price_odometer:
    # Create a scatter plot of price vs odometer
    fig = px.scatter(vehicles_us, x="odometer", y="price")
    st.write("Scatter Plot of Price vs Odometer")
    st.plotly_chart(fig)
    print("This powerful insight shows us evidence for a strong correlation between price and miles driven that influences consumer behavior.")
else:
    st.write("Click the checkbox for viz and insights")

st.divider()

st.header("Statistical Analysis")
st.subheader("Show me the stinkin' p-values then!")

# Create a checkbox to toggle the histogram
show_odometer = st.checkbox("I'm interested in data on odometer readings")
show_model_year = st.checkbox("I'm interested in the distribution of model years")
show_price_odometer = st.checkbox("I'm interested in the relationship between price and odometer reading")
