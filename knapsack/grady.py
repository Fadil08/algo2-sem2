penampung = []
ratio = lambda x, y: round((y/x), 2)
fract = lambda a, b: round((a/b) * b)
kap = int(input("Masukkan kapasitas tas: "))
jum = int(input("Jumlah barang yang ada: "))
o =0
for i in range(jum):
    nama_barang = input('nama barang: ')
    jumlah_barang = int (input ("masukkan jumlah :" ))
    harga_barang = int (input("harga barang [kg]: ")) 
    print ('-'*50)
    penampung.append([o,nama_barang,jumlah_barang,harga_barang])
    o += 1

penampung.sort()
new_list= []

j = 0
for i in penampung:    
    z = ratio(penampung[j][1], penampung[j][2])
    b = penampung.index(i)
    new_list.append((z,b))
    j +=1
print ((new_list))
print("\nBarang yang bisa masuk adalah\n")
print("-"*34)
print("|{:^10}|{:^10}|{:^10}|".format("Nama", "Berat", "Harga"))
print("-"*34)
maxValue = 0
maxWeight = 0
bagcap = 15
bag = bagcap
for i in new_list:
    current = bag
    weight = penampung[i[1]][1] # l[3][1]
    value = penampung[i[1]][2]
    name =penampung[i[1]][3]
    bag -= weight
    if bag >= 0:
        print("|{:^10}|{:^10}|{:^10}|".format(name, str(weight)+"kg", "$"+str(value)))
        maxValue += value
        maxWeight += weight
    # 7 - 12 = -5 < 0
    elif bag < 0:
        bag -= fract(bag, weight) # 7 - (7/12 * 12) = 0
        cwv = round(current/weight*value, 2)
        if cwv == 0:
            break
        else:
            print("|{:^10}|{:^10}|{:^10}|".format(name, str(current)+"/"+str(weight)+"kg", "$"+str(cwv)))
            maxValue += round(current/weight*value, 2)
            maxWeight += round(current/weight, 2)
print("-"*34, "\n")
print("Maka total profit value yang didapat adalah: {}kg dari {}kg dengan ${}\n".format(maxWeight, bagcap, maxValue))
