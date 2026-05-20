import streamlit as st
from dbb_c import conn,cursor
import cloudinary
import cloudinary.uploader
st.title("Media Platform")

cloudinary.config(
    cloud_name=st.secrets["cloud_name"],
    api_key=st.secrets["api_key"],
    api_secret=st.secrets["api_secret"]
)
if "user" not in st.session_state:
    st.session_state.user=None
def dashboard():
    st.sidebar.success("welcome user")
    otp=st.sidebar.selectbox("choose:--",["uploadFiles","viewFiles","Logout"])
    st.header("Dashboard")
    if otp == "uploadFiles":
        st.header("upload ur files here")
        chooseFiles=st.file_uploader("choose file",type=["pdf","mp4","jpg","jpeg","png","mp3"])
        if chooseFiles:
            st.write(chooseFiles.name)
            st.write(chooseFiles.type)
        if "image" in chooseFiles.type:
            st.image(chooseFiles)
        elif "video" in chooseFiles.type:
            st.video(chooseFiles)
        elif "audio" in chooseFiles.type:
            st.audio(chooseFiles)
        
        if st.button("upload file to clodinary"):
            uploaded_dict_obj=cloudinary.uploader.upload(chooseFiles,resource_type="auto")
            url=uploaded_dict_obj["secure_url"]
            st.write(url)
            st.write("file uploaded to cloudinary")
        elif otp=="Logout":
            st.session_state.user=None
            st.success("logout sucessfully")
            st.rerun()

def login_fun():
    st.header("Login")
    with st.form("Login_Form"):
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("Login")
        if btn :
            query="select * from users where email=%s and password = %s"
            values=(email,password)
            cursor.execute(query,values)
            loggedin_user=cursor.fetchone()
            st.session_state.user = loggedin_user
            st.write("loggedin succesfully")
            st.rerun()

def signup_fun():
    st.header("Signup")
    with st.form("SignUp_Form"):
        name=st.text_input("Name")
        email=st.text_input("Email")
        password=st.text_input("Password",type="password")
        btn=st.form_submit_button("SignUp")
        if btn:
                query = """
                INSERT INTO users(name, email, password)
                VALUES(%s, %s, %s)
                """
                values = (name, email, password)
                cursor.execute(query, values)
                conn.commit()
                st.write("user added successfully")

if st.session_state.user==None:
    login,signup=st.tabs(
        ["Login","Signup"]
    )
    with signup:
        signup_fun()
    with login:
        login_fun()
else:
    dashboard()