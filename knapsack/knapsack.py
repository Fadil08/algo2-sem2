import math as mt
penampung = []
konfirmasi = 'y'.lower()
while konfirmasi == 'y':
    nama_barang = input('masukkan barang: ')
    jumlah_barang = int (input ("masukkan jumlah :" ))
    harga_barang = int (input("harga barang [kg]: ")) 
    nilai_barang = mt.floor(harga_barang/jumlah_barang)
    penampung.append([nama_barang,jumlah_barang,harga_barang])
    konfirmasi = input('apakah masih mau menambahkan barang: [y] and [n]: ')
kapasitas_tas=int (input ('masukkan jumlah berat maksimal: '))

print (penampung)
for i in range (len(penampung)):
    if i+1 < len (penampung):
        if penampung[i][3]< penampung [i+1][3]:
            a  = penampung[i]
            b = penampung[i+1]
            penampung[i]= b
            penampung[i+1] = a
    for  j in range (len (penampung)):
        if j +1 < len (penampung):
            if penampung[j][3]< penampung [j+1][3]:
              a  = penampung[i]
            b = penampung[j+1]
            penampung[i]= b
            penampung[j+1] = a   

maxvalue = 0
isitas = []
for i in range (len (penampung)):
    if maxvalue + penampung[i][1] < kapasitas_tas:
        maxvalue += penampung[i][1]
        isitas.append(penampung[i])
    else:
        continue
for i in range (len(isitas)):
    i +=1
    print()
    print(isitas[i][1],"\t", isitas[i][2],"kg")
print("jumlah berat total yang masuk adalah ", maxvalue,"kg dari total kapaistas", kapasitas_tas)

        


        