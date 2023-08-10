import streamlit as st
import pandas as pd
from utils import set_title, set_instructions


set_title("Alma Clinical", "Hot Map")

st.divider()

main_container = st.container()
with main_container:
  st.header("Instructions")
  instructions_expander = st.expander("Expand/Collapse")
  
  with instructions_expander:
    set_instructions()
  
  st.divider()

  tab_all, tab_accent, tab_harmony, tab_duo = st.tabs(["All", "Accent", "Harmony", "Duo"])
    with tab_all:
      st.header("All Devices")

    with tab_accent:
      st.header("Accent")

    with tab_harmony:
      st.header("Harmony")

    with tab_duo:
      st.header("Duo")

uploaded_file = st.file_uploader("CSV Uploader", type=['csv'])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.map(df)
  st.dataframe(df)
  if 'dataframe' not in st.session_state:
    st.session_state.dataframe = df
      
