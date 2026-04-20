import streamlit as st

st.title(f"Привет, {st.session_state.get('user_name', 'Студент')}!")
st.write("Тренажер находится в разработке. Скоро здесь появятся задачи!")

if st.button("Выйти"):
    st.session_state.logged_in = False
    st.rerun()
