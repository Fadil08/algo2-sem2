from time import sleep
import tkinter as tk
import math

window= tk.Tk()
cnv = tk.Canvas(window,width=1000,height=1000)

window.title("Program Rekursif")
inputan = int(input())
case_titik=[]
for i in range(inputan):
    line = input()
    line_x = int(line.split(' ')[0])
    line_y = int(line.split(' ')[1])
    sleep(0.05)
    case_titik.append([i,line_x,line_y])
    cnv.create_text(line_x,line_y,text=int(1)+1)
    cnv.create_oval(line_x-5, line_y-5, line_x+5, line_y+5, fill='yellow')
    window.update()


case_koneksi=[]

while len(case_koneksi) < inputan:
        # point index 0 diset sebagai terhubung / awal mulai
        if len(case_koneksi) == 0:
            case_koneksi.append(0)
            continue
        
        cekcase_titik = -1
        closest_distance =1000
        ceklist_source = []
        ceklist_link = []
        # mencari koneksi point yg memiliki jarak terkecil dengan point-point yg sudah terhubung
        for uc in case_titik:
            index = uc[0]
            if index in case_koneksi:
                continue
            
            x1 = uc[1]
            y1 = uc[2]

            # menghubungkan ke point terdekat yg sudah pernah terhubung
            for c in case_koneksi:
                cpoint = case_titik[c]
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
        case_koneksi.append(ceklist_link[0])
        sleep(0.05)
        cnv.create_line(ceklist_source[1], ceklist_source[2], ceklist_link[1], ceklist_link[2])
        cnv.create_text((ceklist_source[1]+ceklist_link[1])/2,(ceklist_source[2]+ceklist_link[2])/2 ,text=int(ceklist_source[0]))
        window.update()
        sleep(0.05)
       

cnv.pack() 
window.mainloop()
