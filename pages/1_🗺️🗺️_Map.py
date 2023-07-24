import streamlit as st


df=st.session_state.dataframe

st.map(df)

