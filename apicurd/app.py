import streamlit as st
import requests as rq
import pandas as pd
server_loc="http://127.0.0.1:8000"

st.title("CRUD OPERATION")
opt=st.sidebar.selectbox("choose operation:--",["ADD_EMPLOYEE","VIEW_EMPLOYEE","DELETE_EMPLOYEE","UPDATE_EMPLOYEES"])

#--------------add employees----------------
if opt=="ADD_EMPLOYEE":
    st.header("ADD_EMPLOYEE")
    with st.form("adding"):
        name=st.text_input("Name")
        email=st.text_input("email")
        dept=st.selectbox("Department:--",["","IT","Developer","Tester","Sales","Ai engineer"])
        btn=st.form_submit_button("ADD EMPLOYEE")

        if btn:
            new_data={
                "n":name,
                "e":email,
                "d":dept
            }
            res=rq.post(f"{server_loc}/add_emp",json=new_data)
            st.success(res.json()["msg"])

#-----------------veiw employee---------------
elif opt=="VIEW_EMPLOYEE":
    st.header("VIEW_EMPLOYEE")
    res=rq.get(f"{server_loc}/view_emp")
    data=res.json()
    df=pd.DataFrame(data)
    st.dataframe(df)


#---------delete employee--------------
elif opt=="DELETE_EMPLOYEE":
    st.header("DELETE_EMPLOYEE")
    emp_id=st.number_input("enter Employee ID", step=1)
    if st.button("Delete"):
        res=rq.delete(f"{server_loc}/delete_emp/{emp_id}")
        st.success(res.json()["msg"])
        #st.write(res.text)


#-------------------update emp-------------
elif opt=="UPDATE_EMPLOYEES":
    st.header("UPDATE_EMPLOYEE")
    emp_id = st.number_input("Employee ID", step=1)

    name = st.text_input("New Name")
    email = st.text_input("New Email")

    dept = st.selectbox(
        "Department",
        ["IT", "Developer", "Tester", "Sales", "AI Engineer"]
    )

    if st.button("UPDATE"):

        update_data = {
            "n": name,
            "e": email,
            "d": dept
        }

        res = rq.put(
            f"{server_loc}/update_emp/{emp_id}",
            json=update_data
        )

        #st.success(res.json()["msg"])
        st.write(res.text)
    
