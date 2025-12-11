import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.write("Data Analysis")

st.subheader("Data Analysys Using Python & Streamlit")

upload = st.file_uploader("Upload Ypur Dataset (In CSV Format)")

if upload is not None:
    data = pd.read_csv(upload)
    if(st.checkbox("Preview Dataset")):
        if(st.button("Head")):
            st.write(data.head())
        if(st.button("Tail")):
            st.write(data.tail())
if(upload is not None):
    data_shape = st.radio("What Dimension Do You Want to Check",("Row","Columns"))
    if(data_shape=="Row"):
        st.text("Number of Rows")
        st.write(data.shape[0])
    else:
        st.text("Number of Cols")
        st.write(data.shape[1])

if(upload is not None):
    if(data.isnull().values.any()):
        if(st.checkbox("NULL Values in the dataset")):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
            st.success("Congratulation!!!,No Missing Values")
if(upload is not None):
    if(data.duplicated().any()):
        st.warning("This Dataset having Duplicate Values")
        dup = st.selectbox("Do You Want to Remove Duplicate Values?",("Select One","Yes","No"))
        if(dup == "Yes"):
            data = data.drop_duplicates()
            st.text("Duplicate Values are removed")
        else:
            st.text("Ok No Problem")

if(upload is not None):
    if(st.checkbox("Summary of the Dataset")):
        st.write(data.describe(include=all))

if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks to Streamlit")
if(st.checkbox("By")):
    st.success("Amrit Singh")

        

    