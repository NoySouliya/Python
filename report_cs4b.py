from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from subprocess import Popen
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm

pdfmetrics.registerFont(TTFont('F_Lao', 'font/Saysettha OT.ttf'))
pdfmetrics.registerFont(TTFont('F_Eng', 'font/times.ttf'))


def print(c):
    c.setFillColor(colors.red)
    c.setFont('F_Lao', 30)
    c.drawCentredString(148.5*mm, 105*mm, 'ສະບາຍດີ')


c = canvas.Canvas('cs4b.pdf', pagesize=landscape(A4))
print(c)
c.showPage()
c.save()
Popen('cs4b.pdf', shell=True)
