ratio = lambda x, y: round((y/x), 2)
fract = lambda a, b: round((a/b) * b)
listawal = []
kapasitas = int(input("Masukkan kapasitas tas: "))
jumlah  = int(input("Jumlah barang yang ada: "))
o = 0
for i in range(jumlah): # memasukkan data
    nama = input("Nama barang: ")
    berat = int(input("Berat barang (kg): "))
    harga= int(input("Harga barang ($): "))
    print("-"*30)
    listawal.append((o, nama, berat, harga))
    o += 1
listawal.sort()
newlist = []

j = 0
for i in listawal:
    z = ratio(listawal[i][1], listawal[i][2])
    k = listawal.index(i)
    newlist.append((z, k))
    j += 1
newlist.sort(reverse=True)
print("\nBarang yang bisa masuk adalah\n")
print("-"*34)
print("|{:^10}|{:^10}|{:^10}|".format("Nama", "Berat", "Harga"))
print("-"*34)
maxValue = 0
maxWeight = 0
bagan = 15
var  = bagan
for i in newlist:
    current = var
    weight = listawal[i[1]][1] 
    value = listawal[i[1]][2]
    name = listawal[i[1]][3]
    var -= weight
    if var >= 0:
        print("|{:^10}|{:^10}|{:^10}|".format(name, str(weight)+"kg", "$"+str(value)))
        maxValue += value
        maxWeight += weight
    elif var < 0:
        var -= fract(var, weight) 
        cwv = round(current/weight*value, 2)
        if cwv == 0:
            break
        else:
            print("|{:^10}|{:^10}|{:^10}|".format(name, str(current)+"/"+str(weight)+"kg", "$"+str(cwv)))
            maxValue += round(current/weight*value, 2)
            maxWeight += round(current/weight, 2)
print("-"*34, "\n")
print("Maka total profit value yang didapat adalah: {}kg dari {}kg dengan ${}\n".format(maxWeight, bagan, maxValue))
