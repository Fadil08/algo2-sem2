import tkinter as tk

window = tk.TK()
window.title("Graf Labirin")
cnv = tk.Canvas(window,width=1000,height=1000)

titik = int(input())
for i in titik:
    case = input()
    case_x = int(case.split(' ')[0])
    case_y = int(case.split(' ')[1])
    



cnv.pack()
window.mainloop()