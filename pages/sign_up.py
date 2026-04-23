import re
import streamlit as st
from utils import generate_verification_code, send_email, apply_otp_style
from utils import st_funny

conn = st.connection('postgresql', type='sql')

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
    with st.container(border=True):

        #st.markdown("<h3 style='text-align: center;'>Python Gym</h3>", unsafe_allow_html=True)
        
        st_funny('Python Sandbox')
        
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

            with st.spinner('Отправка письма ...'):
                subject = 'Код верификации'
                code = generate_verification_code()
                content = f'Ваш код верификации электронной почты в Python Gym {code}'
                success = send_email(email_input, content, subject)
            
            left_col, center_col, right_col = st.columns([0.3, 0.4, 0.3])
            with center_col:
                apply_otp_style('Код')
                code_input = st.text_input('Код', 
                                           label_visibility='collapsed',
                                           max_chars=4)
        user_login = st.text_input('Придумайте имя пользователя',  
                                   placeholder='Придумайте имя пользователя', 
                                   icon=':material/person:',
                                   label_visibility='collapsed')
        user_password = st.text_input('Установите пароль',  
                                      placeholder='Установите пароль', 
                                      icon=':material/lock:',
                                      label_visibility='collapsed')
        if st.button('Создать аккаунт', width='stretch'):
            pass

        
            




            
          
                
              
 
        
  
