import streamlit as st
import pandas as pd

st.title("Map from File")
st.markdown(
  """Upload a **.csv** file that contains **columns named longitude and latitude** and a map will be displayed.
  """
)

uploaded_file = file_uploader("CSV Uploader", key=uploadedfile, type=['csv'])
if uploaded_file is not None:
  if uploaded_file.type is not 'csv':
    st.error("Invalid file type", icon='🚨')
  else:
    df = pd.read_csv(uploaded_file)
    st.map(df)
    st.dataframe(df)

