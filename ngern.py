import tkinter
from tkinter import ttk
from tkinter import font as tkfont
import pymysql


frm = tkinter.Tk()
frm.geometry("1000x700")
frm.title("Find Data")

def search():
    list_value = ["ນັກສຶກສາທັ້ງໝົດ","ລະຫັດນັກສຶກສາ","ເພດ"]

    combo = cb_search.get()
    text = txt_search.get()

    if(combo == list_value[1]):
        sql_select = "select * from student where s_id='"+text+"';"

    conn.execute(sql_select)

    for i in tree.get_children():
        tree.delete(i)

    i = 0
    for row in conn:
        tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5],))
        i = i + 1


connection = pymysql.connect(host="localhost", user="root", password="", database="cs4b")
conn = connection.cursor()
sql = "select * from student;"
conn.execute(sql)


lb1 = tkinter.Label(frm, text="ຟອມຄົ້ນຫາຂໍ້ມູນນັກສຶກສາ")
lb1.pack(fill="x")
lb1.configure(font=("Saysettha OT", 22), bg="lightgreen")

lb2 = tkinter.Label(frm, text="")
lb2.pack(fill="x", side="bottom")
lb2.configure(font=("Saysettha OT", 22), bg="lightgreen")

lb3 = tkinter.Label(frm, text="ຄົ້ນຫາຂໍ້ມຸູນຕາມ")
lb3.pack()
lb3.configure(font=("Saysettha OT", 16))

combo_list = ["ນັກສຶກສາ", "ລະຫັດນັກສຶກສາ", "ເພດ"]
combo_font = tkfont.Font(family="Saysettha OT", size=16)

cb_search = ttk.Combobox(frm, value=combo_list)
cb_search.pack()
cb_search.configure(font=("Saysettha OT", 16), state="readonly")
cb_search.current(0)
cb_search.option_add("*font", combo_font)

txt_search = tkinter.Entry(frm)
txt_search.pack(pady="30")
txt_search.configure(font=("Saysettha OT", 16))

btn1 = tkinter.Button(frm, text="ຄົ້ນຫາ", width="15",command=search)
btn1.pack(pady="10")
btn1.configure(font=("Saysettha OT", 16), bg="red", fg="black")

st = ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading", foreground="blue", font=("Saysettha OT", 14, "bold"))
st.configure('Treeview', rowheight=30, font=("Saysettha OT", 12))

tree = ttk.Treeview(frm, show="headings")
tree["columns"] = ("1", "2", "3", "4", "5", "6",)
tree.column("#1", width=150)
tree.column("#2", width=200)
tree.column("#3", width=200)
tree.column("#4", width=100)
tree.column("#5", width=150)
tree.column("#6", width=200)


tree.heading("#1", text="ລະຫັດນັກສຶກສາ", anchor="w")
tree.heading("#2", text="ຊື່ນັກສຶກສາ", anchor="w")
tree.heading("#3", text="ນາມສະກຸນ", anchor="w")
tree.heading("#4", text="ເພດ", anchor="w")
tree.heading("#5", text="ວັນເດືອນປີເກີດ", anchor="w")
tree.heading("#6", text="ສາຂາຮຽນ", anchor="w")

i = 0
for row in conn:
    tree.insert('', i, text="", values=(row[0], row[1], row[2], row[3], row[4], row[5],))
    i = i + 1

tree.pack(pady=20)

frm.mainloop()
