from array import array
from cgitb import text
import tkinter as tk
import random
import math
from time import sleep

window = tk.Tk()
window.configure(bg='blue')

# window.attributes('-fullscreen', True)
# window.state('zoomed')

lebar=1300
tinggi=600

cnv = tk.Canvas(window, width=lebar, height=tinggi)
cnv.pack()


list_point = []
list_koneksi = []
jumlah_point =int( input())

def buat_point():
    # buat point secara random
    for i in range(jumlah_point):
        case = input()
        case_x = int(case.split(' ')[0])
        case_y = int(case.split(' ')[1]) 
        x = case_x, lebar
        y = case_y, tinggi
        list_point.append([ x, y])
        # # list_point.append([ i, x, y ])
        # cnv.create_oval(x-5, y-5, x+5, y+5, fill='blue')
        # # window.update()
        # # return list_point
        # print (list_point)
        print('='*10)
        print(list_koneksi)
    buat_titik()
    window.after(gambar_garis)

def buat_titik():
            for i in list_point:
                cnv.create_text(i[0],i[1],text=str[(i[0], i[1])])
            cnv.create_oval(i[0],i[1], i[0]+10, i[1]+10, fill='Blue')


def gambar_garis():
    while len(list_koneksi) < jumlah_point:
        # point index 0 diset sebagai terhubung / awal mulai
        if len(list_koneksi) == 0:
            list_koneksi.append(0)
            continue
        

        ceklist_point = -1
        closest_distance =1000
        ceklist_source = []
        ceklist_link = []
        # mencari koneksi point yg memiliki jarak terkecil dengan point-point yg sudah terhubung
        for uc in list_point:
            index = uc[0]
            if index in list_koneksi:
                continue
            
            x1 = uc[1]
            y1 = uc[2]

            # menghubungkan ke point terdekat yg sudah pernah terhubung
            for c in list_koneksi:
                cpoint = list_point[c]
                x2 = cpoint[1]
                y2 = cpoint[2]
                
                # hitung jarak
                x3 = math.pow(x2 - x1, 2)
                y3 = math.pow(y2 - y1, 2)
                jarak = math.sqrt(x3 + y3)

                # simpan point jika jaraknya lebih kecil dari point sebelumnya
                if jarak < closest_distance:
                    closest_distance = jarak
                    ceklist_source = cpoint
                    ceklist_link = uc
        
        # sudah menemukan point terdekat untuk dihubungkan,
        # gambar ke gui dan simpan ke list point terhubung
        list_koneksi.append(ceklist_link[0])
        cnv.create_line(ceklist_source[1], ceklist_source[2], ceklist_link[1], ceklist_link[2])
        window.update()
        sleep(0.5)

def mulai(args):
    window.unbind('<Visibility>')
    print('mulai')
    print(args)
    window.after(1000, buat_point)

window.bind('<Visibility>', mulai)
print (list_point)

window.mainloop()