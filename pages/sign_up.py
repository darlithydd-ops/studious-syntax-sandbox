import streamlit as st

conn = st.connection('postgresql', type='sql')

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
    with st.container(border=True):
        
        df_groups = conn.query('SELECT id, name FROM groups ORDER BY name;')
        
        selected_group = st.selectbox('Группа',
                                      options=df_groups['name'],
                                      index=1)
        
        selected_group_id = df_groups.loc[df_groups['name'] == selected_group, 'id'].values[0]
        query = 'SELECT full_name FROM users WHERE group_id = :g_id ORDER BY full_name;'
        df_students = conn.query(query, params={'g_id': int(selected_group_id)})
            
        selected_full_name = st.selectbox('Полное имя',
                                          options=df_students['full_name'],
                                          index=1)
  
