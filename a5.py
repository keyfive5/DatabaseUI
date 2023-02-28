import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
  database="testdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdatabase")

root = Tk()
root.title("MySQL Menu")
root.geometry("400x300")

def drop_tables():
  tables = ["table1", "table2", "table3"]
  for table in tables:
    sql = "DROP TABLE IF EXISTS " + table
    mycursor.execute(sql)
    print(table + " dropped")

def create_tables():
  sql = "CREATE TABLE table1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
  mycursor.execute(sql)
  print("table1 created")
  sql = "CREATE TABLE table2 (id INT AUTO_INCREMENT PRIMARY KEY, address VARCHAR(255))"
  mycursor.execute(sql)
  print("table2 created")
  sql = "CREATE TABLE table3 (id INT AUTO_INCREMENT PRIMARY KEY, phone VARCHAR(255))"
  mycursor.execute(sql)
  print("table3 created")

def populate_tables():
  sql = "INSERT INTO table1 (name) VALUES (%s)"
  val = ("John", )
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  sql = "INSERT INTO table2 (address) VALUES (%s)"
  val = ("123 Main St", )
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  sql = "INSERT INTO table3 (phone) VALUES (%s)"
  val = ("555-555-1212", )
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")


def query_tables():
    # Define the SQL queries for each table
    sql_table1 = "SELECT * FROM table1"
    sql_table2 = "SELECT * FROM table2"
    sql_table3 = "SELECT * FROM table3"

    # Execute the queries and fetch the results
    mycursor.execute(sql_table1)
    results_table1 = mycursor.fetchall()
    mycursor.execute(sql_table2)
    results_table2 = mycursor.fetchall()
    mycursor.execute(sql_table3)
    results_table3 = mycursor.fetchall()

    # Print the results to the console
    print("Results from Table 1:")
    for result in results_table1:
        print(result)

    print("Results from Table 2:")
    for result in results_table2:
        print(result)

    print("Results from Table 3:")
    for result in results_table3:
        print(result)

def exit_app():
  root.destroy()

drop_tables_btn = Button(root, text="Drop Tables", command=drop_tables)
drop_tables_btn.pack(pady=10)

create_tables_btn = Button(root, text="Create Tables", command=create_tables)
create_tables_btn.pack(pady=10)

populate_tables_btn = Button(root, text="Populate Tables", command=populate_tables)
populate_tables_btn.pack(pady=10)

query_tables_btn = Button(root, text="Query Tables", command=query_tables)
query_tables_btn.pack(pady=10)

exit_btn = Button(root, text="Exit", command=exit_app)
exit_btn.pack(pady=10)

root.mainloop()

