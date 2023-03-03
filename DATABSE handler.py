from tkinter import *
import sqlite3

# Create tkinter window
root = Tk()
root.title('Database Operations')

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create a table in the database function
def create_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS CUSTOMERS
                   (ID INT PRIMARY KEY NOT NULL,
                   NAME TEXT NOT NULL,
                   AGE INT NOT NULL,
                   EMAIL TEXT);''')
    conn.commit()
    status_label.config(text='Table created successfully')
    print("Table  Created successfully")

# Insert data into the table function
def insert_data():
    id_val = id_entry.get()
    name_val = name_entry.get()
    age_val = age_entry.get()
    email_val = email_entry.get()
    conn.execute("INSERT INTO CUSTOMERS (ID, NAME, AGE, EMAIL) VALUES (?, ?, ?, ?)", (id_val, name_val, age_val, email_val))
    conn.commit()
    status_label.config(text='Data inserted successfully')
    print("Inserted data  successfully")



def read_data():
    # Connect to the database
    conn = sqlite3.connect('example.db')

    # Execute a SELECT statement to retrieve data from the database
    cursor = conn.execute('SELECT * FROM CUSTOMERS')
    data = cursor.fetchall()

    # Display the data in a text box or a table in the Tkinter window
    for row in data:
        print(row)
    status_label.config(text=row)
    # Close the database connection
    conn.close()

    
# Create a Tkinter window with a button to read data from example.db database
button = Button(root, text='Read Data', command=read_data,bg="blue",fg='white')
button.grid(row=6, column=0, columnspan=2, pady=10)



# Create labels, entries, and buttons in the window 
id_label = Label(root, text='ID:',bg="pink")
id_label.grid(row=0, column=0)
id_entry = Entry(root)
id_entry.grid(row=0, column=1)

name_label = Label(root, text='Name:',bg="pink")
name_label.grid(row=1, column=0)
name_entry = Entry(root)
name_entry.grid(row=1, column=1)

age_label = Label(root, text='Age:',bg="pink")
age_label.grid(row=2, column=0)
age_entry = Entry(root)
age_entry.grid(row=2, column=1)

email_label = Label(root, text='Email:',bg="pink")
email_label.grid(row=3, column=0)
email_entry = Entry(root)
email_entry.grid(row=3, column=1)

create_table_button = Button(root, text='Create Table', command=create_table,bg="blue",fg="white")
create_table_button.grid(row=4, column=0)

insert_data_button = Button(root, text='Insert Data', command=insert_data,bg="blue",fg="white")
insert_data_button.grid(row=4, column=1)

status_label = Label(root, text='')
status_label.grid(row=5, columnspan=2)





# create menu bar
menubar = Menu(root)
# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
#Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='GJC Help', command = None)

help_.add_separator()
help_.add_command(label ='About Cs', command = None)



  
 #display Menu
root.config(menu = menubar)
##color of the window
root.configure(background='yellow')
# Start the main loop
root.mainloop()
