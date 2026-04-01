import streamlit as st
import pandas as pd

st.title("ResilienceLens Dashboard")

df = pd.read_csv("data/simulated_data.csv")

st.line_chart(df["latency"])
st.bar_chart(df["failure"].value_counts())