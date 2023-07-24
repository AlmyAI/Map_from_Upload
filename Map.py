import streamlit as st
import pandas as pd


st.title("Map from File")
st.markdown(
  """Upload a **.csv** file that contains **columns named longitude and latitude** and a map will be displayed.
  """
)

uploaded_file = st.file_uploader("CSV Uploader", type=['csv'])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.map(df)
  st.dataframe(df)
  if 'dataframe' not in st.session_state:
    st.session_state.dataframe = df
      
