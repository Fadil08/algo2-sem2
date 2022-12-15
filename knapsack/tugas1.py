ratio = lambda x, y: round((y/x), 2)
fract = lambda a, b: round((a/b) * b)
l = []
bag = int(input("Masukkan kapasitas tas: "))
stuff = int(input("Jumlah barang yang ada: "))
o = 0
for i in range(stuff): 
    p = input("Nama barang: ")
    q = int(input("Berat barang (kg): "))
    r = int(input("Harga barang ($): "))
    print("-"*30)
    l.append((o, q, r, p))
    o += 1
l.sort()
newlist = []

j = 0
for i in l:
    z = ratio(l[j][1], l[j][2])
    k = l.index(i)
    newlist.append((z, k))
    j += 1
newlist.sort(reverse=True)
print("\nBarang yang bisa masuk adalah\n")
print("-"*34)
print("|{:^10}|{:^10}|{:^10}|".format("Nama", "Berat", "Harga"))
print("-"*34)
maxValue = 0
maxWeight = 0
bagcap = 15
bag = bagcap
for i in newlist:
    current = bag
    weight = l[i[1]][1] # l[3][1]
    value = l[i[1]][2]
    name = l[i[1]][3]
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
