import streamlit as st
from dbb_c import conn,cursor
login,signup=st.tabs(
    ["Login","Signup"]
)
with login:
    st.header("Login")
    with st.form("Login_Form"):
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("Login")

with signup:
    st.header("Signup")
    with st.form("SignUp_Form"):
        name=st.text_input("Name")
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("SignUp")
        if btn:

            try:
                # ---------------- INSERT ----------------
                query = """
                INSERT INTO users(name, email, password)
                VALUES(%s, %s, %s)
                """

                values = (name, email, password)

                cursor.execute(query, values)
                conn.commit()

                st.success("Signup Successful 🎉")

                # ---------------- FETCH DATA ----------------
                st.subheader("All Users")

                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()

                st.dataframe(users)

            except Exception as e:
                st.error("Something went wrong")
                st.write(e)
        
