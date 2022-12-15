from curses import window
import tkinter as tk
window = tk.Tk()
window.title("pertemuan 10")

cnv = tk.Canvas(window,width=100,height=600)
cnv.pack()

ukuran = input()
ukuran = ukuran.split(' ')
x = int(ukuran[0])
y = int(ukuran[1])

panjang = 50
y1=50
x1=50
x2 = 50

for i in range(y):
    