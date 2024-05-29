# Import library
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

# Config page
st.set_page_config(
    page_title = "Heart Disease Prediction",
    page_icon="🧊",
    layout = "wide"
)

# Load Data
df = pd.read_csv('Heart_Disease_Prediction.csv')

# Title
st.markdown("<h1 style='text-align: center; color: white;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)

with st.container():
    
    # Dataset
    st.subheader('Dataset')
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        # Sex Correlation 
        chart1 = alt.Chart(df, title='Sex correlation with heart disease').mark_bar().encode(
            column=alt.Column('Sex', header=alt.Header(orient='bottom')),
            y=alt.Y('count(Sex):Q', title="Individuals"),
            x=alt.X('Heart Disease', axis=alt.Axis(labels=False), title=None),
            color=alt.Color('Heart Disease').scale(scheme="lightgreyred").legend(None)
        ).properties(
            height=300,
            width=200
        ).configure_title(fontSize=20)
        st.altair_chart(chart1)

    with col2:
        # Exercise Angine boxplot
        chart2 = alt.Chart(df, title='Exercise Angina correlation with heart disease').mark_bar().encode(
            alt.X("Heart Disease"),
            alt.Y("count(Exercise angina):Q", title="Individuals"),
            alt.Color("Heart Disease").legend(None).scale(scheme="lightgreyred"),
        ).properties(
        height=450,
        width=300
        )
        st.altair_chart(chart2)

