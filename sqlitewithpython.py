import sqlite3
connection=sqlite3.connect("new.db")
cursor=connection.cursor()
def  create_table_employee():
    cursor.execute("""
    CREATE TABLE   IF NOT EXISTS employee(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   full_name VARCHAR(200) NOT NULL,
                   salary INTEGER)
                   """)
def get_all_employee():
    data=cursor.execute("SELECT * FROM employee")
    return data.fetchall()

def insert_row_employee(full_name,salary):
    if(get_name(full_name)==None):
        cursor.execute("""
        INSERT INTO employee(full_name,salary) VALUES(?,?) 
                   """,(full_name,salary))
def get_by_id(id):
    data=cursor.execute("SELECT *FROM  employee where id =?",(id,))
    return data.fetchone()
def get_name(name):
    data=cursor.execute("SELECT full_name FROM  employee where full_name =?",(name,))
    return data.fetchone()
if __name__=='__main__':
    create_table_employee()
    insert_row_employee('jalol',20000)
    insert_row_employee("dilshod",20000)
    connection.commit()
print(get_all_employee())
print(get_by_id(1))
cursor.close()