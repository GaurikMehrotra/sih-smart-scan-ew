import streamlit as st
import pandas as pd

st.title("DRDO Smart Scan Strategy")

df = pd.read_csv("simulator/ew_dataset.csv")

st.subheader("RF Activity Dataset")
st.dataframe(df.head(20))

st.subheader("Band Activity")

band_activity = (
    df.groupby("band")["active"]
    .sum()
    .reset_index()
)

st.bar_chart(
    band_activity.set_index("band")
)

st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "85%")

with col2:
    st.metric("Precision", "84.6%")

with col3:
    st.metric("Recall", "81.5%")