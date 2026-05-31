from fastapi import FastAPI
import mysql.connector


conn_obj=mysql.connector.connect(
    host="localhost",
    database="api_crud",
    user="root",
    password="root"
)
cursor_obj=conn_obj.cursor(dictionary=True)


app=FastAPI()

@app.post("/add_emp")

def add_employee(new_data: dict):
    name=new_data["n"]
    email=new_data["e"]
    department=new_data["d"]
    query=""" insert into emps(name,email,department) values(%s,%s,%s)"""
    values=(name,email,department)
    cursor_obj.execute(query,values)
    conn_obj.commit()
    return{"msg":"Employee Added Sucessfully"}


@app.get("/view_emp")
def view_employee():
    query="SELECT * FROM emps"
    cursor_obj.execute(query)
    data=cursor_obj.fetchall()
    return data

@app.delete("/delete_emp/{emp_id}")
def delete_employee(emp_id: int):
    query="DELETE FROM emps WHERE id=%s"
    cursor_obj.execute(query,(emp_id,))
    conn_obj.commit()
    return{"msg":"Employee deleted sucessfully"}

@app.put("/update_emp/{emp_id}")
def update_employee(emp_id: int, new_data: dict):

    name = new_data["n"]
    email = new_data["e"]
    department = new_data["d"]

    query = """
    UPDATE emps
    SET name=%s, email=%s, department=%s
    WHERE id=%s
    """

    values = (name, email, department, emp_id)

    cursor_obj.execute(query, values)

    conn_obj.commit()

    return {"msg": "Employee Updated Successfully"}