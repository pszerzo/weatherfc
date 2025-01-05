import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
x = st.selectbox("Select data for x axis", ["GDP", "Generosity", "Happiness"]).lower()
y = st.selectbox("Select data for y axis", ["GDP", "Generosity", "Happiness"]).lower()
st.subheader(f"{x} and {y}")

df = pd.read_csv("happy.csv")
xvalues = df[x]
yvalues = df[y]

graph = px.scatter(x=xvalues, y=yvalues, labels={"x": x, "y": y})
st.plotly_chart(graph)