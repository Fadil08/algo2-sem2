from posixpath import split
import tkinter as tk
import math

window= tk.Tk()

def inptitik(n):
    case_titik = []
    for noUrut in range(n):
        titik = input()
        x= int(titik.split(' ')[0])
        y= int(titik.split(' ')[1])
        cnv.create_oval(x-10,y+10,x+10,y-10,fill='green')
        cnv.create_text(x,y,text=noUrut)
        case_titik.append([x,y])
   
    return case_titik
def koneksi_titik():
    inpkoneksi = int(input())
    titikconeksi= []
    for i in range (len(inpkoneksi)):
        line_case2 = input()
        x = int(line_case2.split()[0])
        y = int(line_case2.split()[1])
        z = int(line_case2.split()[2])
        titikconeksi.append([x,y,z])
        


cnv = tk.Canvas(window,width=1000,height=1000)
cnv.pack()
window.mainloop()