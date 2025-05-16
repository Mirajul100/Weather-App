import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(layout="centered" , page_title="Weather App")

st.title("Weather Forecast for the next days")

input = st.text_input(label="place" , placeholder="Enter the place").capitalize()
# slider = st.slider(label="Forecast Days" , min_value=1 , max_value=5)
select = st.selectbox("Select data to view" 
             , ("Temperature" , "Sky")
             , index=None 
             , placeholder="Select the value")

# st.subheader(f"{select} for the next {slider} days in {input}")
st.subheader(f"{select} for the days in {input}")

data = get_data(input , select)

if select == "Temperature":
        temperature = data["main"]["temp"]
        temperature = int(temperature - 273)
        st.subheader(f"The Temperature of {input} is {temperature:2}°C")
        #figure = px.line(x=dates , y=temperature , labels={"x":"Dates" , "y":"Temperature (C)"})
        #st.plotly_chart(figure)
if select =="Sky":
        pull_data = data["weather"][0]["main"]
        st.subheader(f"The weather of country {input} is {pull_data}")
        if pull_data == "Clouds":
                st.image("image/c.png")

