import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", 1, 5, 1, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", options=["Temperature", "Sky"])
st.subheader(f"{option} for the next {days} in {place}")

dates = ["01.01.", "01.02.", "01.03.", "01.04.", "01.05"]
temperatures = [23, 19, 21, 26, 25]

dates = dates[:days+1]
temperatures = temperatures[:days+1]

graph = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(graph)
