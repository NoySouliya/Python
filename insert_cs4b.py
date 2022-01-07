import tkinter
from tkinter import ttk
from tkinter import font as tkfont
import os
import pymysql
from tkinter import messagebox

frm = tkinter.Tk()
frm.title("Insert Student")
frm.geometry('500x700')

def insert():
    connection = pymysql.connect(host="localhost", user="root", password="", database="cs4b")
    conn = connection.cursor()

    id = en.get()
    name = en1.get()
    surname = en2.get()
    birthday = en3.get()
    major = cbMajor.get()

    if(v1.get() == 1):
        gender = "ຊາຍ"
    else:
        gender = "ຍິງ"


    value = messagebox.askquestion("ການຢືນຢັນ", "ທ່ານຕ້ອງການເພີ່ມຂໍ້ມູນແທ້ ຫຼື ບໍ ?")
    if (value == 'yes'):
        sql_insert = "insert into student values" \
                      "('"+id+"', '"+name+"', '"+surname+"', '"+gender+"', '"+birthday+"', '"+major+"');"
        conn.execute(sql_insert)
        connection.commit()

        frm.withdraw()
        os.system("Database.py")


def back():
    frm.withdraw()
    os.system("Database.py")



lb = tkinter.Label(frm, text="ຟອມເພີ່ມຂໍ້ມູນນັກສຶກສາ")
lb.pack()
lb.config(font=("Saysettha OT", 22), fg="red")

lb1 = tkinter.Label(frm, text="ລະຫັດນັກສຶກສາ:")
lb1.place(x=20, y=100)
lb1.config(font=("Saysettha OT", 16))

lb2 = tkinter.Label(frm, text="ຊື່:")
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

lb6 = tkinter.Label(frm, text="ສາຂາຮຽນ:")
lb6.place(x=20, y=500)
lb6.config(font=("Saysettha OT", 16))

# Entry

en = tkinter.Entry(frm)
en.place(x=200, y=100)
en.config(font=("Saysettha OT", 16))

en1 = tkinter.Entry(frm)
en1.place(x=200, y=180)
en1.config(font=("Saysettha OT", 16))

en2 = tkinter.Entry(frm)
en2.place(x=200, y=260)
en2.config(font=("Saysettha OT", 16))

en3 = tkinter.Entry(frm)
en3.place(x=200, y=420)
en3.config(font=("Saysettha OT", 16))

# RadioButton

v1 = tkinter.IntVar()

rd1 = tkinter.Radiobutton(frm, text="ຊາຍ", variable=v1, value=1)
rd1.place(x=200, y=340)
rd1.config(font=("Saysettha OT", 16))

rd2 = tkinter.Radiobutton(frm, text="ຍິງ", variable=v1, value=2)
rd2.place(x=330, y=340)
rd2.config(font=("Saysettha OT", 16))

# ComboList

cbList = ["ໄອທີ", "ນິເທດສາດ", "ການທະນາຄານ", "ບໍລິຫານທຸລະກິດ"]
cbFont = tkfont.Font(family="Saysettha OT", size=16)

cbMajor = ttk.Combobox(frm, width=15, value=cbList)
cbMajor.place(x=200, y=500)
cbMajor.config(font=("Saysettha OT", 16), state="readonly")
cbMajor.current(0)
cbMajor.option_add("*font", cbFont)

btn = tkinter.Button(frm, text="ເພີ່ມຂໍ້ມູນ", width=10, command=insert)
btn.place(x=100, y=600)
btn.config(font=('Saysettha OT', 16), bg="#b6b6b4", fg="black")

btn2 = tkinter.Button(frm, text="ກັບຄືນ", width=10, command=back)
btn2.place(x=300, y=600)
btn2.config(font=('Saysettha OT', 16), bg="red", fg="white")

frm.mainloop()
