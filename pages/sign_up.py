import streamlit as st

conn = st.connection('postgresql', type='sql')

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
    with st.container(border=True):
        with st.expander():
            df_groups = conn.query('SELECT name FROM groups ORDER BY name;')
            selected_group = st.selectbox("Выберите группу для работы:",
                                          options=df_groups['name'],
                                          index=None,
                                          placeholder="Выберите вариант или введите название...")
      
  
