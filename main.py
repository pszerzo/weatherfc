import streamlit as st

st.title("Weather Forecast for the Next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", 1, 5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", options=["Temperature", "Sky"])
st.subheader(f"{option} for the next {days} in {place}")
