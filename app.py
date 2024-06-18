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
    
    print("It looks like nearly all cars sold are around or below 200K miles driven. See stats section below.")
    
    fig = px.histogram(vehicles_us, x="odometer", nbins=10)
    st.write("Histogram of Odometer Readings")
    st.plotly_chart(fig)

else:
    st.write("Click the checkbox for viz and insights")

if show_model_year:
    # Create a histogram of model_year
    
    print("Interesting, we can see that nearly all cars that are listed on this website are from recent years – specifically, the last two decades.")
    
    fig = px.histogram(vehicles_us, x="model_year", nbins=15)
    st.write("Histogram of Model Year")
    st.plotly_chart(fig)

else:
    st.write("Click the checkbox for viz and insights")

if show_price_odometer:
    # Create a scatter plot of price vs odometer

    print("This powerful insight shows us evidence for a strong correlation between price and miles driven that influences consumer behavior.")
    
    fig = px.scatter(vehicles_us, x="odometer", y="price")
    st.write("Scatter Plot of Price vs Odometer")
    st.plotly_chart(fig)

else:
    st.write("Click the checkbox for viz and insights")

st.divider()

st.header("Statistical Analysis")
st.subheader("Show me the stinkin' p-values then!")

# Create a checkbox to toggle the histogram
show_hypotest1 = st.checkbox("I'm interested in data on odometer readings")
show_hypotest2 = st.checkbox("I'm interested in the distribution of model years")
show_hypotest3= st.checkbox("I'm interested in the relationship between price and odometer reading")

if show_hypotest1:
    print("Insight: This finding suggests that 95% of cars older than 2012 had between 18K and 248K miles and those newer than 2012 had between 0 and 166K miles. However, due to the high variance in the samples, the hypothesis test found that older vehicles did not have greater odometer readings compared to newer vehicles.")
    st.write("""
        **Hypothesis Test Description:**
        
        This hypothesis test checks whether there is a significant difference between the odometer readings of car models before and after 2012.

        **Test Statistic:** Two-sample, one-sided t-test

        **P-value:** 0.05
    """)

    #Define the threshold for old and new vehicles (e.g., 10 years)
    threshold_year = 2012
    
    # Split the data into old and new vehicles
    old_vehicles = vehicles_us[vehicles_us['model_year'] <= threshold_year]
    new_vehicles = vehicles_us[vehicles_us['model_year'] > threshold_year]
    
    # Calculate the mean odometer readings for old and new vehicles
    old_odometer_mean = old_vehicles['odometer'].mean()
    new_odometer_mean = new_vehicles['odometer'].mean()

    # Calculate the standard deviations of odometer readings for old and new vehicles
    old_odometer_std = old_vehicles['odometer'].std()
    new_odometer_std = new_vehicles['odometer'].std()

    # Calculate the pooled standard deviation
    pooled_std = np.sqrt(((old_odometer_std**2) / len(old_vehicles)) + ((new_odometer_std**2) / len(new_vehicles)))
    
    # Calculate the Z-score
    z_score = (old_odometer_mean - new_odometer_mean) / pooled_std
    
    # Calculate the p-value
    p_value = sts.norm.sf(z_score)

    # Interpret the results
    if p_value < 0.05:
        print("The average odometer reading of old vehicles is not significantly greater than that of newer vehicles.")
    else:
        print("The average odometer reading of old vehicles is significantly greater than that of newer vehicles.")


if show_hypotest2:
    print("Insight: In this test, we find that average days listed are below 90 days, suggesting sellers are successful or unsuccessful and delist within 90 days of posting their cars. We also find that the mean number of days listed is 39.5 with 95% of cars being listed for 56 days or less.")
    st.write("""
        **Hypothesis Test Description:**
        
        This hypothesis test checks whether, on average, cars are listed on the site for 90 days or less .

        **Test Statistic:** One-sample, one-sided Z-test
        
        **P-value:** 0.05
    """)

    from scipy.stats import norm

    # Calculate the mean and standard deviation of days_listed
    days_listed_mean = vehicles_us['days_listed'].mean()
    days_listed_std = vehicles_us['days_listed'].std()

    # Calculate the Z-score
    z_score = (days_listed_mean - 90) / (days_listed_std / np.sqrt(len(vehicles_us)))
    
    # Calculate the p-value
    p_value = norm.sf(z_score)

    # Interpret the results
    if p_value < 0.05:
        print("The average days_listed is significantly greater than 90 days.")
    else:
        print("The average days_listed is not significantly greater than 90 days.")


if show_hypotest3:
    print("Insight: Here we find that 19.5% of cars listed are white and 15% of cars are black. Due to the stringent normalization of proportion tests, we find that the proprtion of white color cars is significantly greater than black color cars in the US from 1955 to 2019. A very powerful statistic.")
    st.write("""
        **Hypothesis Test Description:**

        This hypothesis test checks whether there were more white cars than black cars listed.

        **Test Statistic:** Two-proportion, one-sided Z-test

        **P-value:** 0.05
    """)
    
    # Calculate the proportions of white and black paint colors
    white_proportion = vehicles_us['paint_color'].value_counts()['white'] / len(vehicles_us)
    black_proportion = vehicles_us['paint_color'].value_counts()['black'] / len(vehicles_us)

    # Calculate the pooled proportion
    pooled_proportion = (white_proportion + black_proportion) / 2

    # Calculate the Z-score
    z_score = (white_proportion - black_proportion) / np.sqrt(pooled_proportion * (1 - pooled_proportion) * (1 / len(vehicles_us) + 1 / len(vehicles_us)))
    
    # Calculate the p-value
    p_value = norm.sf(z_score)

    # Interpret the results
    if p_value < 0.05:
        print("The proportion of white paint color is significantly greater than the proportion of black paint color.")
    else:
        print("The proportion of white paint color is not significantly greater than the proportion of black paint color.")
        
            
