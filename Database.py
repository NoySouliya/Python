import pymysql
import tkinter as tk
from tkinter import ttk
import os
from tkinter import font as tkfont

frm = tk.Tk()
frm.title('Database')
frm.geometry('1200x700')

connection = pymysql.connect(host="localhost", user="root", password="", database="cs4b")
conn = connection.cursor()
sql = "select * from student;"
conn.execute(sql)

def save_update():
    txtId.config(state="normal")

    n_id = txtId.get()
    n_name = txtName.get()
    n_surname = txtSurname.get()
    n_bd = txtBd.get()
    n_major = cbMajor.get()

    if(v1.get() == 1):
        n_gender = 'ຊາຍ'
    else:
        n_gender = 'ຍິງ'

    sql_update = "update student set name='"+n_name+"', surname='"+n_surname+"', gender='"+n_gender+"', birthday='"+n_bd+"', major='"+n_major+"' where stid='"+n_id+"';"
    conn.execute(sql_update)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from student;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        i += 1





def update():
    data = tree.selection()
    value = tree.item(data)['values'][0]

    sql_select = "select * from student where stid='"+value+"';"
    conn.execute(sql_select)

    for row in conn:
        o_id = row[0]
        o_name = row[1]
        o_surname = row[2]
        o_gender = row[3]
        o_bd = row[4]
        o_major = row[5]

        txtId.insert(0, o_id)
        txtName.insert(0, o_name)
        txtSurname.insert(0, o_surname)
        txtBd.insert(0, o_bd)

        if (o_gender == "ຊາຍ"):
            rdm.select()
        else:
            rdf.select()

        cbList = ["ໄອທີ", "ນິເທດສາດ", "ການທະນາຄານ", "ບໍລິຫານທຸລະກິດ"]
        if (o_major == cbList[0]):
            cbMajor.current(0)

        elif(o_major == cbList[1]):
            cbMajor.current(1)

        elif(o_major == cbList[2]):
            cbMajor.current(2)

        elif(o_major == cbList[3]):
            cbMajor.current(3)

        btn3.config(state="disabled")
        txtId.config(state="disabled")




def delete():
    data = tree.selection()
    value = tree.item(data)['values'][0]
    #print(value)

    sql_delete = "delete from student where stid = '"+value+"';"
    conn.execute(sql_delete)
    connection.commit()

    for i in tree.get_children():
        tree.delete(i)

    sql_select = "select * from student;"
    conn.execute(sql_select)

    i=0
    for row in conn:
        tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        i += 1

def open():
    frm.withdraw()
    os.system("insert_cs4b.py")



st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", foreground="blue", font=("Saysettha OT", 16))
st.configure('Treeview', rowheight=30, font=("Saysettha OT", 14))

tree = ttk.Treeview(frm)
tree['columns'] = ('1', '2', '3', '4', '5', '6')

tree.column('#0', width=0)
tree.column('#1', width=100)
tree.column('#2', width=200)
tree.column('#3', width=200)
tree.column('#4', width=100)
tree.column('#5', width=200)
tree.column('#6', width=200)

tree.heading('#1', text='ລະຫັດ', anchor='w')
tree.heading('#2', text='ຊື່', anchor='w')
tree.heading('#3', text='ນາມສະກຸນ', anchor='w')
tree.heading('#4', text='ເພດ', anchor='w')
tree.heading('#5', text='ວັນເດືອນປີເກີດ', anchor='w')
tree.heading('#6', text='ສາຂາຮຽນ', anchor='w')


i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    i = i+1

tree.place(x=10, y=100)

lb1 = tk.Label(frm, text='ລາຍຊື່ນັກສຶກສາທັງໝົດ')
lb1.place(x=300, y=20)
lb1.config(font=("Saysettha OT",20), fg="red")

btn1 = tk.Button(frm, text="ເພີ່ມຂໍ້ມູນ", width=10, command=open)
btn1.place(x=300, y=500)
btn1.config(font=("Saysettha OT", 16, 'bold'), bg="lightblue", fg="black")

btn2 = tk.Button(frm, text="ລົບຂໍ້ມູນ", width=10, command=delete)
btn2.place(x=500, y=500)
btn2.config(font=("Saysettha OT", 16, 'bold'), bg="red", fg="white")

btn3 = tk.Button(frm, text="ແກ້ໄຂຂໍ້ມູນ", width=10, command=update)
btn3.place(x=700, y=500)
btn3.config(font=("Saysettha OT", 16, 'bold'), bg="purple", fg="white")

############################################################################

frm.geometry('1600x700')

lb2 = tk.Label(frm, text="ຟອມແກ້ໄຂຂໍ້ມູນນັກສຶກສາ")
lb2.place(x=1150, y=20)
lb2.configure(font=("Saysettha OT", 20), fg="red")

lb2 = tk.Label(frm, text="ລະຫັດນັກສຶກສາ")
lb2.place(x=1100, y=150)
lb2.configure(font=("Saysettha OT", 14))

lb3 = tk.Label(frm, text="ຊື່ນັກສຶກສາ")
lb3.place(x=1100, y=220)
lb3.configure(font=("Saysettha OT", 14))

lb4 = tk.Label(frm, text="ນາມສະກຸນ")
lb4.place(x=1100, y=280)
lb4.configure(font=("Saysettha OT", 14))

lb8 = tk.Label(frm, text="ເພດ")
lb8.place(x=1100, y=340)
lb8.configure(font=("Saysettha OT", 14))

lb6 = tk.Label(frm, text="ວັນເດືອນປີເກີດ")
lb6.place(x=1100, y=400)
lb6.configure(font=("Saysettha OT", 14))

lb7 = tk.Label(frm, text="ສາຂາຮຽນ")
lb7.place(x=1100, y=460)
lb7.configure(font=("Saysettha OT", 14))

txtId = tk.Entry(frm)
txtId.place(x=1230, y=150)
txtId.config(font=("Saysettha OT", 14))

txtName = tk.Entry(frm)
txtName.place(x=1230, y=220)
txtName.config(font=("Saysettha OT", 14))

txtSurname = tk.Entry(frm)
txtSurname.place(x=1230, y=280)
txtSurname.config(font=("Saysettha OT", 14))

v1 = tk.IntVar()

rdm = tk.Radiobutton(frm, text="ຊາຍ", variable=v1, value=1)
rdm.place(x=1230, y=340)
rdm.configure(font=("Saysettha OT", 14))

rdf = tk.Radiobutton(frm, text="ຍິງ", variable=v1, value=2)
rdf.place(x=1340, y=340)
rdf.configure(font=("Saysettha OT", 14))

txtBd = tk.Entry(frm)
txtBd.place(x=1230, y=400)
txtBd.configure(font=("Saysettha OT", 14))

cbList = ["ໄອທີ", "ນິເທດສາດ", "ການທະນາຄານ", "ບໍລິຫານທຸລະກິດ"]
cbFont = tkfont.Font(family="Saysettha OT", size=14)

cbMajor = ttk.Combobox(frm, width=15, value=cbList)
cbMajor.place(x=1230, y=460)
cbMajor.config(font=("Saysettha OT", 14), state="readonly")
cbMajor.current(0)
cbMajor.option_add("*font", cbFont)

btn = tk.Button(frm, text="ບັນທຶກການແກ້ໄຂ", command=save_update)
btn.place(x=1230, y=520)
btn.configure(font=("Saysettha OT", 14), bg="powderblue")

frm.mainloop()
