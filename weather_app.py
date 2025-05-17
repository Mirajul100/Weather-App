import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_data


# Add title , text input , selecbox

st.set_page_config(layout="centered" , page_title="Weather App" , page_icon="image/c.png")
st.title("Weather Forecast for Country/city current day")

input = st.text_input(label="Country or City" , placeholder="Enter the place").capitalize()

select = st.selectbox("Select data to view" 
             , ("Temperature" , "Sky")
             , index=None 
             , placeholder="Select the value")

st.subheader(f"{select} for the days in {input}")

data = get_data(input , select)
if input:

        try:

                if select == "Temperature":
                        temperature = data["main"]["temp"]
                        temperature = int(temperature - 273)
                        st.subheader(f"The Temperature of {input} is {temperature:2}°C")

                if select =="Sky":
                        w_data = data["weather"][0]["main"]
                        pull_data = [data["weather"][0]["main"]]
                        st.subheader(f"The weather of country {input} is {w_data}")
                        image_list = {"Clear": "image/clear.png"
                                ,"Clouds": "image/cloud.png"
                                ,"Rain": "image/rain.png","Snow": "image/snow.png"}
                        
                        cap = {"Clear":"Clear"
                        ,"Clouds":"Clouds"
                        ,"Rain" : "Rain" , "Snow" : "Snow"}
                        
                        images = [image_list[condition] for condition in pull_data]
                        caption = [cap[i] for i in pull_data]
                        st.image(images , width=150 , output_format="PNG" , caption=caption)

        except KeyError:
                st.error("This place in not exists")
        except TypeError:
                st.error("This place in not exists")