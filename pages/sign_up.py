import streamlit as st

conn = st.connection('postgresql', type='sql')

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
    with st.container(border=True):
        df_groups = conn.query('SELECT name FROM groups ORDER BY name;')
        selected_group = st.selectbox('Группа',
                                      options=df_groups['name'],
                                      index=None,
                                      placeholder='Группа',
                                      label_visibility='collapsed')
        
      
  
