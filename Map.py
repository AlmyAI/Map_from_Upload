import streamlit as st
import pandas as pd
from utils import set_title, set_instructions


set_title("Alma Clinical", "Hot Map")
set_instructions()


uploaded_file = st.file_uploader("CSV Uploader", type=['csv'])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.map(df)
  st.dataframe(df)
  if 'dataframe' not in st.session_state:
    st.session_state.dataframe = df
      
