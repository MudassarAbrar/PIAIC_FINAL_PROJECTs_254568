import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('TITLE DASHBOARD')

uploaded_file = st.file_uploader("Choose a CSV file",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader('Data Preview')
    st.write(df.head())#just writes the first 5 rows of the data
    
    
    st.subheader('Data Summary')
    st.write(df.describe())
    
    
    
    st.subheader("Filter Data")
    
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select Column to filter by ',columns)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox('Select Value',unique_values)    
    
    filtered_data = df[df[selected_column] == selected_values]
    st.write(filtered_data)
    
    
    
    st.subheader("Plot Data")
    x_column = st.selectbox('Select x-axis',columns)
    y_column = st.selectbox('Select y-axis',columns)
    
    if st.button("Generate Plot"):
       st.line_chart(filtered_data.set_index(x_column)[y_column])
       
       
       
else:
    st.write("Please upload a file")