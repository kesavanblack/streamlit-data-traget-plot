import streamlit as st
import pandas as pd
import plotly.express as px

# File uploader for CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    data = pd.read_csv(uploaded_file)
    st.dataframe(data.head())
    
    # Get columns list
    columns = list(data.columns)
    
    # Select target column for color encoding
    target = st.selectbox('Choose a target:', columns)
    
    # Remove target column from available X and Y options
    col2 = columns.copy()
    col2.remove(target)
    
    # Select variables for X and Y axes
    x_var = st.selectbox('Choose an X variable:', col2)
    y_var = st.selectbox('Choose a Y variable:', col2)
    
    # Select plot type
    plot_type = st.selectbox('Choose plot type:', ['Scatter', 'Line', 'Bar','pie','histogram'])
    
    # Generate plot based on selected plot type
    if plot_type == 'Scatter':
        fig = px.scatter(data, x=x_var, y=y_var, color=target)
    elif plot_type == 'Line':
        fig = px.line(data, x=x_var, y=y_var, color=target)
    elif plot_type == 'Bar':
        fig = px.bar(data, x=x_var, y=y_var, color=target)
    elif plot_type == 'pie':
         fig = px.pie(data, x=x_var, y=y_var, color=target)
    elif plot_type == 'histogram':
        fig = px.histogram(data, x=x_var, y=y_var, color=target)
    
    # Display the plot
    st.plotly_chart(fig)
