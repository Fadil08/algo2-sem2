import tkinter as tk
import math

def segitiga(cnv,lvl,curlvl,panjang,titikA):
    ax = 550
    ay = 50
    if lvl == curlvl:
        return
    if curlvl == 1:
        panjang = 100

        bx = math.cos(math.radians(60)) * panjang
        by = math.sin(math.radians(60)) * panjang

        cnv.create_line(ax,ay,ax+bx,ay+by) 
        cnv.create_text(ax,ay, text= 'A')
    else:
        print('segitiga kecil')
        # segitiga(cnv,lvl,curlvl+1)


lvl = int(input('level: '))

window= tk.Tk()
cnv = tk.Canvas(window,width=1000,height=500)
cnv.pack()

panjang = 350
ax = 550
ay = 50
segitiga(cnv,lvl,1,panjang, (ax,ay) )
cnv.pack()
window.mainloop()