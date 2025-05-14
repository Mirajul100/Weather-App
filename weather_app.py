import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="centered" , page_title="Weather App")

st.title("Weather Forecast for the next days")

input = st.text_input(label="place" , placeholder="Enter the place")
slider = st.slider(label="Forecast Days" , min_value=1 , max_value=5)
select = st.selectbox("Select data to view" 
             , ("Temperature" , "Sky" )
             , index=None 
             , placeholder="Select the value")

st.subheader(f"{select} for the next {slider} days in {input}")

dates = ["2022-24-10" , "2022-25-2=10" , "2022-26-10"]
temperature = [10 , 30 , 40]

figure = px.line(x=dates , y=temperature , labels={"x":"Dates" , "y":"Temperature (C)"})
st.plotly_chart(figure)