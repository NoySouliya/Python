import tkinter as tk
import pymysql
from tkinter import ttk
import os
from tkinter import messagebox


frm = tk.Tk()
frm.title('Display Customer')
frm.geometry('1200x700')

connection = pymysql.connect(host="localhost", user="root", password="", database="cs4b3")
conn = connection.cursor()
sql = "select * from customer;"
conn.execute(sql)

def delete():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    sql_delete = "delete from customer where c_id = '"+value+"';"
    conn.execute(sql_delete)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from customer;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        i += 1



def open():
    frm.withdraw()
    os.system("test2.py")

def ex():
    value=messagebox.askquestion("Result", "ເຈົ້າຕ້ອງການອອກຈາກໂປຣແກຣມແທ້ ຫຼື ບໍ່?")
    if(value == 'yes'):
        exit()

ct = ttk.Style()
ct.theme_use("clam")
ct.configure("Treeview.Heading", foreground="blue", font=("Saysettha OT", 16))
ct.configure('Treeview', rowheight=30, font=("Saysettha OT", 14))

tree = ttk.Treeview(frm)
tree['columns'] = ('1', '2', '3', '4', '5', '6', '7')

tree.column('#0', width=0)
tree.column('#1', width=100)
tree.column('#2', width=150)
tree.column('#3', width=150)
tree.column('#4', width=100)
tree.column('#5', width=200)
tree.column('#6', width=200)
tree.column('#7', width=200)

tree.heading('#1', text='ລະຫັດ', anchor='w')
tree.heading('#2', text='ຊື່', anchor='w')
tree.heading('#3', text='ນາມສະກຸນ', anchor='w')
tree.heading('#4', text='ເພດ', anchor='w')
tree.heading('#5', text='ວັນເດືອນປີເກີດ', anchor='w')
tree.heading('#6', text='ທີ່ຢູ່', anchor='w')
tree.heading('#7', text="ເບີໂທລະສັບ", anchor='w')

i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    i = i+1

tree.place(x=10, y=100)


btn1 = tk.Button(frm, text="ເພີ່ມຂໍ້ມູນ", width=10, command=open)
btn1.place(x=300, y=500)
btn1.config(font=("Saysettha OT", 16, 'bold'), bg="lightblue", fg="black")

btn2 = tk.Button(frm, text="ລົບຂໍ້ມູນ", width=10, command=delete)
btn2.place(x=500, y=500)
btn2.config(font=("Saysettha OT", 16, 'bold'), bg="red", fg="white")

btn3 = tk.Button(frm, text="ອອກຈາກໂປຣແກຣມ", width=20, command=ex)
btn3.place(x=700, y=500)
btn3.config(font=("Saysettha OT", 16, 'bold'), bg="green", fg="white")

lb1 = tk.Label(frm, text='ລາຍຊື່ລູກຄ້າທັງໝົດ')
lb1.place(x=300, y=20)
lb1.config(font=("Saysettha OT", 20), fg="red")

frm.mainloop()
