import tkinter
from tkinter import ttk
from tkinter import font as tkf
import pymysql

a=tkinter.Tk()
a.geometry("1000x700")
a.title("CS4B_search Data")

def ff():
   list_srk=["ນັກສຶກສາທັງໝົດ","ລະຫັດນັກສຶກສາ","ເພດ"]

   combo=srk.get()
   text= txt_srk.get()

   if(combo == list_srk[1]):
       sql_select= "select * from student where stid='"+text+"';"
   elif(combo == list_srk[2]):
       sql_select= "select * from student where gender='"+text+"';"
   elif(combo == list_srk[0]):
       sql_select= "select * from student;"
   conn.execute(sql_select)


   for i in tree.get_children():
       tree.delete(i)

   i=0
   for row in conn:
       tree.insert('',i,text='',value=(row[0],row[1],row[2],row[3],row[4],row[5]))
       i=i+1

#jark database
connection=pymysql.connect(host="Localhost",user="root",password="",database="cs4b")
conn=connection.cursor()
sql="select *from student;"
conn.execute(sql)

combo_font=tkf.Font(family="Saysettha OT",size=16)

#label
lb1=tkinter.Label(a,text="ຟອມຄົ້ນຫາຂໍ້ມູນນັກສຶກສາ")
lb1.pack(fill='x')
lb1.configure(font=("Saysettha OT",22),bg="lightblue")

lb2=tkinter.Label(a,text="")
lb2.pack(fill='x',side='bottom')
lb2.configure(font=("Saysettha OT",22),bg="pink")

lb3=tkinter.Label(a,text="ຄົ້ນຫາຂໍ້ມູນຕາມ")
lb3.pack()
lb3.configure(font=("Saysettha OT",18))

#listttttt
list_srk=["ນັກສຶກສາທັງໝົດ","ລະຫັດນັກສຶກສາ","ເພດ"]

#combo
srk= ttk.Combobox(a,value=list_srk)
srk.pack()
srk.configure(font=("Saysettha OT",18),state="readonly")
srk.current(0)
srk.option_add("*font",combo_font)

#entry
txt_srk=tkinter.Entry(a)
txt_srk.pack(pady=20)
txt_srk.configure(font=("Saysettha OT",16))

#button
bt_srk=tkinter.Button(a,text="ຄົ້ນຫາ",width=15,command=ff)
bt_srk.pack()
bt_srk.configure(font=("Saysettha OT",16),bg="blue",fg="white")

#treeview
st=ttk.Style()
st.theme_use("clam")
st.configure("Treeview.Heading",font=("Saysettha OT",14,"bold"))
st.configure("Treeview",rowheight=30,font=("Saysettha OT",14))

tree=ttk.Treeview(a,show="headings")
tree["columns"]=("1","2","3","4","5","6")
tree.pack(pady=10)

tree.column("#1",width=150)
tree.column("#2",width=180)
tree.column("#3",width=180)
tree.column("#4",width=110)
tree.column("#5",width=180)
tree.column("#6",width=180)

tree.heading("#1",text="ລະຫັດນັກສຶກສາ")
tree.heading("#2",text="ຊື່ນັກສຶກສາ")
tree.heading("#3",text="ນາມສະກຸນ")
tree.heading("#4",text="ເພດ")
tree.heading("#5",text="ວັນເດືອນປີເກີດ")
tree.heading("#6",text="ສາຂາຮຽນ")


i=0
for row in conn:
   tree.insert('',i,text='',value=(row[0],row[1],row[2],row[3],row[4],row[5]))
   i=i+1

tree.pack(pady=20)



a.mainloop()
