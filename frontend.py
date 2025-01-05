import streamlit as st
import plotly.express as px

import backend
from backend import get_data

st.title("Weather Forecast for the Next days")
place = st.text_input("Place: ")
days = int(st.slider("Forecast days", 1, 5, help="Select the number of forecasted days"))
option = st.selectbox("Select data to view", options=["Temperature", "Sky"])
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:

        filtered_data = get_data(place, days)

        if option == "Temperature":
            temp = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            # for i in sky:
            #     sky[i] = "images/" + sky[i] + ".png"
            # alternative:
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky]
            st.image(image_paths, width=150)
            #dates = [dict["dt_txt"] for dict in filtered_data]

    except KeyError:
        ("Non existing location")