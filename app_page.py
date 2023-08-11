import streamlit as st

def set_title(varTitle, varSubtitle):
    st.markdown(f"""# {varTitle} <span style=color:#7ab3ba><font size=5>{varSubtitle}</font></span>""",unsafe_allow_html=True)
    

def set_instructions(varInstructions):
    instruction_expander = st.expander("Collapse/Expand Instructions", expanded=True)
    with instruction_expander:
        st.subheader("Instructions")
        st.markdown(varInstructions)

    st.divider()
