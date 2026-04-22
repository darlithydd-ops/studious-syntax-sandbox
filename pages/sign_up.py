import streamlit as st

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
  with st.container(border=True):
    st.header('ok')
  
