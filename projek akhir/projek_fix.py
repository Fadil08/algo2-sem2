from tkinter import *
import tkinter.font

root = Tk()
root.title("Fisk-py")
root.geometry("500x500")

# mengatur ukuran font
thefont = tkinter.font.Font(size=10)

# membuat sebuah frame baru
frame = LabelFrame(root,text="Fisika-py",padx=20,pady=20, )
frame.place(x =25 , y = 20 )

# membuat kotak input nomor
inputan1 = Entry(frame,width=15)
hasil = Entry(frame,width=15)
inputan2 =Entry(frame,width=15)
inputan3 =Entry(frame,width=15)
inputan1["font"] = thefont
hasil["font"] = thefont
inputan2["font"] = thefont
inputan3["font"] = thefont
hasil.insert(0, "0")
inputan3.insert(0,"0")
inputan1.grid(row=1,column=0)
inputan2.grid(row=3,column=0)
inputan3.grid(row=5,column=0)
hasil.grid(row=1, column=2)

# membuat labelnya colom
labelrms1 = Label(frame,text="")
labelrms2 = Label(frame,text="")
labelrms3 = Label(frame,text="")

labelrms1.grid(row=0, column=0)
labelrms2.grid(row=2,column=0)
labelrms3.grid(row=4, column=0)
# menuliskan rumus dan semua fungsi
rmslbl = Label(frame,text="Formula",bg="yellow")
rmslbl.grid(row=11,column=0)

rmsnya = Label(frame,text="")
rmsnya.grid(row=12,column=0)

chek = {"rumus","yes"}
def rumus(rm):
    # hapus tulisan pada kotak 2
    hasil.delete(0,END)
    
    # mendapatkan nilai dari kotak
    kotaksatu = cliked.get()
    inp1 = float(inputan1.get())
    inp2 = float(inputan2.get())
    inp3 = float(inputan3.get())

    # menghilangkan tulisan sebelumnya 
    global rmsnya
    global labelrms1
    global labelrms2
    global labelrms3

    if "rumus" in chek:
        rmsnya.place_forget()
    else:
        pass
      
    # menuliskan rumus dan menentukan hitungan
    if kotaksatu == "kecepatan":
        labelrms1 = Label(frame,text="Jarak")
        labelrms2 = Label(frame, text="waktu")
        lblsatuan = Label(frame, text="Km/jam")
        hitungan = inp1 / inp2  # jarak /waktu
        rmsnya = Label(frame,text="kecepatan = jarak / waktu \n V = S / T \n V ="+inputan1.get()+"/"+inputan2.get()+" = "+str(hitungan)+" V")
    elif kotaksatu == "percepatan":
        labelrms1 = Label(frame,text="kecepatan")
        labelrms2 = Label(frame, text="waktu")
        lblsatuan = Label(frame, text="M/s")
        hitungan = inp1 /inp2 # (a) = (v)  kecepatan / (t) waktu
        rmsnya = Label(frame,text="pecepatan = jarak / waktu \n V = S / t \n V = "+inputan1.get()+"/"+inputan2.get()+" = "+str(hitungan)+" V")
    elif kotaksatu == "waktu":
        labelrms1 = Label(frame,text="Jarak")
        labelrms2 = Label(frame, text="kecepatan")
        lblsatuan = Label(frame, text="jam")
        hitungan = inp1 /inp2 # jarak / kecepatan
        rmsnya = Label(frame,text="waktu = jarak / kecepatan \n t = S x V  \n"+inputan1.get()+"/"+inputan2.get()+" = "+str(hitungan)+" Sekon")
    elif kotaksatu == "volume":
        labelrms1 = Label(frame,text="panjang")
        labelrms2 = Label(frame, text="lebar")
        labelrms3 = Label(frame, text="tinggi")
        lblsatuan = Label(frame, text="M3")
        hitungan = inp1 * inp2 * inp3 # (V) = (p) panjang  x (l) lebar x (t) tinggi
        rmsnya = Label(frame,text="volume = panjang x lebar x tinggi \n v = P x L x T \n"+inputan1.get()+" x "+inputan2.get()+" x "+inputan3.get()+"= "+str(hitungan)+" V")
    elif kotaksatu == "massa": # (ρ) = massa (m) / volume (v) = kg (m-3)
        labelrms1 = Label(frame,text="gaya")
        labelrms2 = Label(frame,text="percepatan")
        lblsatuan = Label(frame, text="Kg")
        hitungan = inp1 /inp2
        rmsnya = Label(frame,text="massa = gaya / percepatan \n m = f / a \n"+inputan1.get()+"/"+inputan2.get()+" = "+str(hitungan)+"Kg ")
    elif kotaksatu == "gaya":
        labelrms1 = Label(frame,text="massa")
        labelrms2 = Label(frame, text="percepatan")
        lblsatuan = Label(frame, text="M/s2")
        hitungan = inp1 * inp2 # massa x percepatan = newton : f = m x a
        rmsnya = Label(frame,text="gaya = massa x percepatan \n f = m x a \n"+inputan1.get()+"/"+inputan2.get()+" = "+str(hitungan)+" N")
    elif kotaksatu == "energi potensial":
        labelrms1 = Label(frame,text="massa")
        labelrms2 = Label(frame, text="gravitasi")
        labelrms3 = Label(frame, text="tinggi")
        lblsatuan = Label(frame, text="J")
        hitungan = inp1 * inp2 * inp3 # ep = m x g x h(tinggi)
        rmsnya = Label(frame,text="Ep = massa x gravitasi x tinggi \n Ep = M x G x H\n Ep = "+inputan1.get()+" x "+inputan2.get()+" x "+inputan3.get()+" = "+str(hitungan)+" Ep")
    elif kotaksatu == "jarak":
        labelrms1 = Label(frame,text="kecepatan")
        labelrms2 = Label(frame, text="waktu")
        lblsatuan = Label(frame, text="M/s")
        hitungan = inp1 * inp2
        rmsnya = Label(frame,text="jarak = kecepatan x waktu \n S = V x T\n S= "+inputan1.get()+"/"+inputan2.get()+" = "+str(hitungan)+" km/j")
    hasil_akhir = hitungan
    hasil.insert(0,hasil_akhir)
    rmsnya.grid(row=13, column=0)
    labelrms1.grid(row=0, column=0)
    labelrms2.grid(row=2,column=0)
    labelrms3.grid(row=4, column=0)
    lblsatuan.grid(row=1,column=3)
    

# memasukkan nilai untuk membuat pilihan rumus fisika
option = ["kecepatan","percepatan","waktu","jarak","volume", "massa", "gaya","energi potensial"]
cliked = StringVar()
cliked.set(option[0])
drop = OptionMenu(frame,cliked,*option,command=rumus)
drop.config(width=20)
drop.grid(row = 2,column=2)

for i in cliked.get():
    if cliked.get() == "kecepatan":
        labelrms1 = Label(frame,text="Jarak").grid(row=0, column=0)
        labelrms2 = Label(frame, text="waktu").grid(row=2,column=0)
    elif cliked.get() == "percepatan":
        labelrms1 = Label(frame,text="kecepatan").grid(row=0, column=0)
        labelrms2 = Label(frame, text="waktu").grid(row=2,column=0)
    elif cliked.get() == "waktu":
        labelrms1 = Label(frame,text="Jarak").grid(row=0, column=0)
        labelrms2 = Label(frame, text="kecepatan").grid(row=2,column=0)
    elif cliked.get() == "jarak":
        labelrms1 = Label(frame,text="kecepatan").grid(row=0, column=0)
        labelrms2 = Label(frame, text="waktu").grid(row=2,column=0)
    elif cliked.get() == "volume":
        labelrms1 = Label(frame,text="panjang").grid(row=0, column=0)
        labelrms2 = Label(frame, text="lebar").grid(row=2,column=0)
        labelrms3 = Label(frame, text="tinggi").grid(row=4, column=0)
    elif cliked.get() == "massa":
        labelrms1 = Label(frame,text="gaya").grid(row=0, column=0)
        labelrms2 = Label(frame, text="percepatan").grid(row=2,column=0)
    elif cliked.get() == "gaya":
        labelrms1 = Label(frame,text="massa").grid(row=0, column=0)
        labelrms2 = Label(frame, text="percepatan").grid(row=2,column=0)
    elif cliked.get() == "energi potensial":
        labelrms1 = Label(frame,text="massa").grid(row=0, column=0)
        labelrms2 = Label(frame, text="gravitasi").grid(row=2,column=0)
        labelrms2 = Label(frame, text="tinggi").grid(row=4, column=0)

#membuat tombol menghitung

btn = Button(frame,text="count",command=lambda:rumus("hitung"))
btn.grid(row = 3,column=2)
root.mainloop()