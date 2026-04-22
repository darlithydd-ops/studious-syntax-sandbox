import streamlit as st

st.set_page_config(page_title='Python Gym', layout='wide')

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
  
login_page = st.Page('pages/login.py', title='Вход в систему', icon='🐍')
sign_up_page = st.Page('pages/sign_up.py', title='Вход в систему', icon='🐍')
trainer_page = st.Page('pages/trainer.py', title='Тренажер', icon='🐍')

if st.session_state.logged_in:
    pg = st.navigation([trainer_page])
else:
    pg = st.navigation([login_page])

pg.run()
