import streamlit as st

conn = st.connection('postgresql', type='sql')

left_col, center_col, right_col = st.columns([0.35, 0.3, 0.35])

with center_col:
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center;'>Python Gym</h2>", 
                    unsafe_allow_html=True)
        login_input = st.text_input('Логин', 
                                   placeholder='Введите ваш логин', 
                                   icon=':material/person:',
                                   label_visibility='collapsed')
        pass_input = st.text_input('Пароль', 
                                   type='password', 
                                   placeholder='Введите ваш пароль', 
                                   icon=':material/lock:',
                                   label_visibility='collapsed')
        if st.button('Войти', width='stretch'):
            user = conn.query(
            "SELECT id, full_name FROM users WHERE login = :l AND password_hash = :p",
            params={"l": login_input, "p": pass_input}
            )
            if not user.empty:
                st.session_state.logged_in = True
                st.session_state.user_name = user['full_name'].iloc[0]
                st.session_state.user_id = int(user['id'].iloc[0])
                st.success("Успешный вход!")
                st.rerun()
            else:
                st.error("Неверный логин или пароль")
        st.markdown("""
            <style>
                hr {
                    margin-top: 0rem !important;   /* Отступ сверху */
                    margin-bottom: 1rem !important; /* Отступ снизу */}
            </style>""",
            unsafe_allow_html=True)
        st.divider()
        if st.button('Создать аккаунт', width='stretch'):
            pg = st.navigation(['sign_up'])
        st.markdown("---")
        if st.button('Востановить доступ', width='stretch'):
            pass
