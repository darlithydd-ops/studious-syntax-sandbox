import re
import utils
import streamlit as st

conn = st.connection('postgresql', type='sql')

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
    with st.container(border=True):

        st.markdown("<h2 style='text-align: center;'>Python Gym</h2>", 
                    unsafe_allow_html=True)
        
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
        
        raw_email_input = st.text_input('Почта (необходима для восстановления доступа)',  
                                        placeholder='example@mail.com', 
                                        icon=':material/mail:')
        
        if raw_email_input:
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
            email_input = raw_email_input.strip()
            if not re.match(email_pattern, email_input):
                st.error('Неверный формат электронной почты')
        
        if st.button('Отправить код верификации', width='stretch'):

            subject = 'Код верификации'
            content = f'Ваш код верификации электронной почты в Python Gym {1234}'
            success = utils.send_email(email_input, content, subject)
            
            with st.form('jhn'):
                c_1, c_2, c_4, c_6, c_8, c_9 = st.columns([1, 1, 1, 1, 1, 1])
                with c_2:
                    digit_1 = st.text_input('digit_1', 
                                            label_visibility='collapsed', 
                                            max_chars=1, 
                                            key='d1')
                with c_4:
                    digit_2 = st.text_input('digit_2', 
                                            label_visibility='collapsed', 
                                            max_chars=1, 
                                            key='d2')
                with c_6:
                    digit_3 = st.text_input('digit_3', 
                                            label_visibility='collapsed', 
                                            max_chars=1, 
                                            key='d3')
                with c_8:
                    digit_4 = st.text_input('digit_4', label_visibility='collapsed', 
                                            max_chars=1, 
                                            key='d4')
                submitted = st.form_submit_button("Подтвердить код")
 
        
  
