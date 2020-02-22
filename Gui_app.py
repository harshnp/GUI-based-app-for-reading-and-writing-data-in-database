from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(name,age,address):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="harsh123")
    print("connected!")
    cur = conn.cursor()

    query = '''insert into student(name,age,address) values (%s,%s,%s); '''
    cur.execute(query,(name,age,address))
    print("Data Added!")
    conn.commit()
    conn.close()

def search_data(myid):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="harsh123")
    #print("connected!")
    cur = conn.cursor()

    query = '''select * from student where id=%s; '''
    cur.execute(query,(myid))
    row = cur.fetchone()
   # print(row)
    display_result(row)
    conn.commit()
    conn.close()

def display_result(result):
    listbox = Listbox(frame,height=1,width=20)
    listbox.grid(row=9,column=2)
    listbox.insert(END,result)

def display_all():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="harsh123")
    cur = conn.cursor()

    query = '''select * from student ; '''
    cur.execute(query,())
    row = cur.fetchall()
    
    listbox = Listbox(frame,height=7,width=20)
    listbox.grid(row=11,column=2)
    for x in row:
        listbox.insert(END,x)
    
    conn.commit()
    conn.close()


canvas = Canvas(root,height=500,width=250)
canvas.pack()

frame = Frame()
frame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.8)

label0 = Label(frame,text="Add Data")
label0.grid(row=0,column=2)

label1 = Label(frame,text="Name: ")
label1.grid(row=1,column=1)
entry_name = Entry(frame)
entry_name.grid(row=1,column=2)

Label(frame,text="Age: ").grid(row=2,column=1)
entry_age = Entry(frame)
entry_age.grid(row=2,column=2)

Label(frame,text="Address: ").grid(row=3,column=1)
entry_address = Entry(frame)
entry_address.grid(row=3,column=2)

button1 = Button(frame,text="Click to add data!",command=lambda:get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button1.grid(row=4,column=2)

Label(frame,text="***Search Data***").grid(row=5,column=2)
Label(frame,text="Search By Id: ").grid(row=6,column=1)
search_id = Entry(frame)
search_id.grid(row=6,column=2)

button2 = Button(frame,text="Search!",command=lambda:search_data(search_id.get()))
button2.grid(row=7,column=2)
button3 = Button(frame,text="Show All",command=lambda:display_all())
button3.grid(row=8,column=2)

root.mainloop()
