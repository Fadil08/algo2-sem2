from cgitb import text
from struct import pack
import tkinter as tk
import math


window = tk.Tk()

cnv= tk.Canvas(window,width=1000,height=500)
cnv.pack()
panjang = 100

ax = 350
ay = 50

bx = math.cos(math.radians(60)) * panjang
by = math.sin(math.radians(60)) * panjang

cnv.create_line(ax,ay,ax+bx,ay+by) 
cnv.create_text(ax,ay, text= 'A')
cnv.create_text(ax+bx,ay+by, text='B')

cx= math.cos(math.radians(120))* panjang
cy= math.sin(math.radians(120))* panjang

# cnv.create_line(ax+cx, ay+cy, ax+bx, ay+by)
cnv.create_text(ax+cx,ay+cy,text='C')

# cnv.create_line(ax+cx, ay+cy, ax,ay)



window.mainloop()