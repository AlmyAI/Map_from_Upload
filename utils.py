import streamlit as st
import streamlit.components.v1 as c
from streamlit_elements import elements, mui, html

def set_title(varTitle, varSubtitle):
  st.markdown(f"""# {varTitle} <span style=color:#7ab3ba><font size=5>{varSubtitle}</font></span>""",unsafe_allow_html=True)
  

def set_instructions():
  st.markdown("""Upload a **.csv** file that contains **columns named longitude and latitude** and a map will be displayed.""")
  st.divider()
