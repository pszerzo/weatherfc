import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next days")
place = st.text_input("Place: ")
days = int(st.slider("Forecast days", 1, 5, help="Select the number of forecasted days"))
option = st.selectbox("Select data to view", options=["Temperature", "Sky"])
st.subheader(f"{option} for the next {days} days in {place}")

result = get_data(place, days, option)
dates = ["01.05.", "01.06.", "01.07.", "01.08.", "01.09"]
dates = dates[:days]

graph = px.line(x=dates, y=result, labels={"x": "Date", "y": "Temperature (C)"})
if option == "Temperature":
    st.plotly_chart(graph)
elif option == "Sky":
    st.write(result)