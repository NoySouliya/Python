import tkinter
from tkinter import font as tkfont
from tkinter import ttk
import pymysql
import os
from tkinter import messagebox


frm = tkinter.Tk()
frm.title("Insert Student")
frm.geometry('500x800')


def insert():
    connection = pymysql.connect(host="localhost", user="root", password="", database="cs4b3")
    conn = connection.cursor()

    id = ent.get()
    name = ent1.get()
    surname = ent2.get()
    birthday = ent3.get()
    location = cbLoca.get()
    tel = ent4.get()

    if(v1.get() == 1):
        gender = "ຊາຍ"
    else:
        gender = "ຍິງ"


    value = messagebox.askquestion("ການຢືນຢັນ", "ທ່ານຕ້ອງການເພີ່ມຂໍ້ມູນແທ້ ຫຼື ບໍ ?")
    if (value == 'yes'):
        sql_insert = "insert into customer values" \
                      "('"+id+"', '"+name+"', '"+surname+"', '"+gender+"', '"+birthday+"', '"+location+"','"+tel+"');"
        conn.execute(sql_insert)
        connection.commit()

        frm.withdraw()
        os.system("Test1.py")


def back():
    frm.withdraw()
    os.system("Test1.py")

# label

lb = tkinter.Label(frm, text="ຟອມເພີ່ມຂໍ້ມູນລູກຄ້າ")
lb.pack()
lb.config(font=("Saysettha OT", 22), fg="red")

lb1 = tkinter.Label(frm, text="ລະຫັດນັກລູກຄ້າ:")
lb1.place(x=20, y=100)
lb1.config(font=("Saysettha OT", 16))

lb2 = tkinter.Label(frm, text="ຊື່ລູກຄ້າ:")
lb2.place(x=20, y=180)
lb2.config(font=("Saysettha OT", 16))

lb3 = tkinter.Label(frm, text="ນາມສະກຸນ:")
lb3.place(x=20, y=260)
lb3.config(font=("Saysettha OT", 16))

lb4 = tkinter.Label(frm, text="ເພດ:")
lb4.place(x=20, y=340)
lb4.config(font=("Saysettha OT", 16))

lb5 = tkinter.Label(frm, text="ວັນເດືອນປີເກີດ:")
lb5.place(x=20, y=420)
lb5.config(font=("Saysettha OT", 16))

lb6 = tkinter.Label(frm, text="ທີ່ຢູ່:")
lb6.place(x=20, y=500)
lb6.config(font=("Saysettha OT", 16))

lb7 = tkinter.Label(frm, text="ເບີໂທລະສັບ:")
lb7.place(x=20, y=580)
lb7.config(font=("Saysettha OT", 16))

# Entry

ent = tkinter.Entry(frm)
ent.place(x=200, y=100)
ent.config(font=("Saysettha OT", 16))

ent1 = tkinter.Entry(frm)
ent1.place(x=200, y=180)
ent1.config(font=("Saysettha OT", 16))

ent2 = tkinter.Entry(frm)
ent2.place(x=200, y=260)
ent2.config(font=("Saysettha OT", 16))

ent3 = tkinter.Entry(frm)
ent3.place(x=200, y=420)
ent3.config(font=("Saysettha OT", 16))

ent4 = tkinter.Entry(frm)
ent4.place(x=200, y=580)
ent4.config(font=("Saysettha OT", 16))

# RadioButton

v1 = tkinter.IntVar()

rd1 = tkinter.Radiobutton(frm, text="ຊາຍ", variable=v1, value=1)
rd1.place(x=200, y=340)
rd1.config(font=("Saysettha OT", 16))

rd2 = tkinter.Radiobutton(frm, text="ຍິງ", variable=v1, value=2)
rd2.place(x=330, y=340)
rd2.config(font=("Saysettha OT", 16))

# ComboList

cbList = ["ວຽງຈັນ", "ນະຄອນຫຼວງ", "ຊຽງຂວາງ", "ຫຼວງພະບາງ", "ຈຳປະສັກ", "ບໍ່ແກ້ວ"]
cbFont = tkfont.Font(family="Saysettha OT", size=16)

cbLoca = ttk.Combobox(frm, width=15, value=cbList)
cbLoca.place(x=200, y=500)
cbLoca.config(font=("Saysettha OT", 16), state="readonly")
cbLoca.current(0)
cbLoca.option_add("*font", cbFont)

btn = tkinter.Button(frm, text="ເພີ່ມຂໍ້ມູນ", width=10, command=insert)
btn.place(x=100, y=700)
btn.config(font=('Saysettha OT', 16), bg="#b6b6b4", fg="black")

btn2 = tkinter.Button(frm, text="ກັບຄືນ", width=10, command=back)
btn2.place(x=300, y=700)
btn2.config(font=('Saysettha OT', 16), bg="red", fg="white")


frm.mainloop()
