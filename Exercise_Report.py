from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from subprocess import Popen
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
import pymysql

connection = pymysql.connect(host="localhost", user="root", password="", database="n1")
conn = connection.cursor()
sql = "select * from student where s_id='ST001';"
conn.execute(sql)

pdfmetrics.registerFont(TTFont('F_Lao', 'font/Saysettha OT.ttf'))
pdfmetrics.registerFont(TTFont('F_Eng', 'font/times.ttf'))


def print(c):
    c.setFillColor(colors.blue)
    c.setFont('F_Lao', 30)
    c.drawCentredString(148.5*mm, 190*mm, 'ບັດເຂົ້າຫ້ອງສອບເສັງ (ນັກສຶກສາໃໝ່)')

    c.setFillColor(colors.black)
    c.setFont('F_Lao', 22)
    c.drawString(50*mm, 170*mm, 'ລະຫັດນັກສຶກສາ:')
    c.drawString(50*mm, 150*mm, 'ຊື່ນັກສຶກສາ:')
    c.drawString(50*mm, 130*mm, 'ນາມສະກຸນ:')
    c.drawString(50*mm, 110*mm, 'ເພດ:')
    c.drawString(50*mm, 90*mm, 'ວັນ/ເດືອນ/ປີເກີດ:')
    c.drawString(50*mm, 70*mm, 'ເບີໂທລະສັບ:')
    c.drawString(50*mm, 50*mm, 'ອີເມວ:')
    c.drawString(50*mm, 30*mm, 'ສາຂາຮຽນ:')

    c.setFillColor(colors.green)
    c.setFont('F_Lao', 16)
    c.drawCentredString(200*mm, 10*mm, 'ກະລຸນາແຈ້ງບັດກ່ອນເຂົ້າຫ້ອງສອບເສັງ')


c = canvas.Canvas('Exercise.pdf', pagesize=landscape(A4))

text = c.beginText(110*mm, 170*mm)
text.setFillColor(colors.red)
text.setFont('F_Lao', 22)
text.setLeading(57)

for data in conn:
    for line in data:
        text.textLine(line)
        c.drawText(text)

print(c)
c.showPage()
c.save()
Popen('Exercise.pdf', shell=True)
