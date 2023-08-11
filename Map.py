import streamlit as st
from app_page import set_instructions, set_title
from app_functions import get_dataframe, filter_dataframe

st.set_page_config(page_title="Alma Clinical", layout="wide")

# 0. Set Variables 
dfAll = get_dataframe("all", False)
dfAccent = get_dataframe("accent_prime", False)
dfHarmony = get_dataframe("harmony", False)
dfOpus = get_dataframe("opus", False)
dfSoprano = get_dataframe("soprano", False)
varLat = "Latitude"
varLong = "Longitude"

# 1. Set Page Title
page_title = "Alma Clinical"
page_subtitle = "Hot Map"
set_title(page_title, page_subtitle)

# 2. Set Page Instructions
page_instructions = """Use the **tabs** below to navigate hot maps for all devices or individual devices. Each tab contains **a map and data table**. The data is **filterable**."""
set_instructions(page_instructions)

# 3. Set Page Tabs
main_container = st.container()
with main_container:
    tabAll, tabAccent, tabHarmony, tabOpus, tabSoprano = st.tabs(["All Devices", "Accent Prime", "Harmony", "Opus Plasma", "Soprano"],)

    with tabAll: 
        expander_map_all = st.expander("Collapse/Expand", expanded=True)
        with expander_map_all:
            st.subheader("Hot Map - All Devices")
            st.map(dfAll, latitude="Latitude", longitude="Longitude", color="Color")

        expander_data_all = st.expander("Collapse/Expand", expanded=True)
        with expander_data_all:
            st.subheader("Data - All Devices")
            st.dataframe(dfAll, use_container_width=True)

    with tabAccent: 
        expander_map_accent = st.expander("Collapse/Expand", expanded=True)
        with expander_map_accent:
            st.subheader("Hot Map - Accent-Prime")
            st.map(dfAccent, latitude="Latitude", longitude="Longitude")

        expander_data_accent = st.expander("Collapse/Expand", expanded=True)
        with expander_data_accent:
            st.subheader("Data - Accent Prime")
            st.dataframe(dfAccent, use_container_width=True)

    with tabHarmony: 
        expander_map_harmony = st.expander("Collapse/Expand", expanded=True)
        with expander_map_harmony:
            st.subheader("Hot Map - Harmony")
            st.map(dfHarmony, latitude="Latitude", longitude="Longitude")

        expander_data_harmony = st.expander("Collapse/Expand", expanded=True)
        with expander_data_harmony:
            st.subheader("Data - Harmony")
            st.dataframe(dfHarmony, use_container_width=True)

    with tabOpus: 
        expander_map_opus = st.expander("Collapse/Expand", expanded=True)
        with expander_map_opus:
            st.subheader("Hot Map - Opus Plasma")
            st.map(dfOpus, latitude="Latitude", longitude="Longitude")

        expander_data_opus = st.expander("Collapse/Expand", expanded=True)
        with expander_data_opus:
            st.subheader("Data - Opus Plasma")
            st.dataframe(dfOpus, use_container_width=True)

    with tabSoprano: 
        expander_map_opus = st.expander("Collapse/Expand", expanded=True)
        with expander_map_opus:
            st.subheader("Hot Map - Soprano")
            st.map(dfSoprano, latitude="Latitude", longitude="Longitude")

        expander_data_opus = st.expander("Collapse/Expand", expanded=True)
        with expander_data_opus:
            st.subheader("Data - Soprano")
            dfSoprano_filtered = st.dataframe(filter_dataframe(dfSoprano, "dfsopranofiltered"), use_container_width=True)

        
