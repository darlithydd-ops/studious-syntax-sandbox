import streamlit as st

conn = st.connection('postgresql', type='sql')

#st.title("Добро пожаловать в Тренажер")

tab_login, tab_reg = st.tabs(["Вход", "Регистрация"])

with tab_login:
    left_col, right_col = st.columns([0.3, 0.7])
    with left_col:
        with st.container(border=True):
            login_input = st.text_input("Логин")
            pass_input = st.text_input("Пароль", type="password")
            if st.button("Войти"):
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

with tab_reg:
    st.subheader("Создание аккаунта")
    
    # Подгружаем группы из БД
    groups_df = conn.query("SELECT id, name FROM groups")
    group_names = groups_df['name'].tolist()
    
    selected_group = st.selectbox("Выберите вашу группу", group_names)
    
    # ID выбранной группы
    g_id = int(groups_df[groups_df['name'] == selected_group]['id'].iloc[0])
    
    # Подгружаем студентов этой группы
    students_df = conn.query(
        "SELECT full_name FROM users WHERE group_id = :gid AND is_registered = False",
        params={"gid": g_id}
    )
    
    if not students_df.empty:
        fio = st.selectbox("Ваше ФИО", students_df['full_name'])
        new_login = st.text_input("Придумайте логин", key="reg_login")
        new_pass = st.text_input("Придумайте пароль", type="password", key="reg_pass")
        
        if st.button("Зарегистрироваться"):
            # Обновляем запись в базе
            with conn.session as s:
                s.execute(
                    "UPDATE users SET login = :l, password_hash = :p, is_registered = True WHERE full_name = :fio",
                    {"l": new_login, "p": new_pass, "fio": fio}
                )
                s.commit()
            st.success("Вы успешно зарегистрированы! Теперь войдите во вкладке Вход.")
    else:
        st.info("В этой группе нет свободных мест.")

