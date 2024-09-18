import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: File Uploader
st.title('Data and Target Plotting App')

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Step 2: Load the Data
    df = pd.read_csv(uploaded_file)
    st.write("Preview of the data:", df.head())

    # Step 3: Select the target and features to plot
    target_col = st.selectbox('Select Target Column', df.columns)
    feature_col = st.selectbox('Select Feature to Plot', df.columns)

    # Step 4: Create the plot
    if st.button('Plot'):
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[feature_col], y=df[target_col], ax=ax)
        ax.set_title(f'{feature_col} vs {target_col}')
        st.pyplot(fig)
