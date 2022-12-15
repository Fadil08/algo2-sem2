list1 = []

kapasitas = int(input('kapasitas barang: '))
jum = int(input('jumlah barang: '))

char = 0
for i in range(jum):
    a = input('nama barang: ')
    b = float(input('Jumlah Barang[kg]: '))
    c = float(input('Harga Barang[$]: '))
    hasil = c/b
    char +=1
    list1.append({
        "nama":a,
        "berat": b,
        "harga": c,
        "value": hasil
    })

list1.sort(key=lambda x: x["value"], reverse=True) # 1543 1345
print ('-'*60)
print("NO. \t nama barang \t Barat barang\t Harga barang\t value")
print ('-'*60)

for i in list1:
    print("{}\t\t{}\t\t{}\t\t{}\t{}".format(list1.index(i)+1,i["nama"], i["berat"],i["harga"],i["value"]))
print ('-'*60)

listbaru = []
hargatotal = 0
kapasitas_masuk = 0
for i in list1:
    if kapasitas >= i["berat"]:
        if i["value"] > 0:
            kapasitas -= i["berat"]
            hargatotal += i["harga"]
            kapasitas_masuk += i["berat"]
            listbaru.append(i)
# hasil
print ('hasil Knapsack')
print ('-'*60)
for i in listbaru:
    print("{},\t{}\t{}\t{}\t{}".format(listbaru.index(i)+1, i["nama"], i["berat"], i["harga"], i["value"] ))

print(f"Kapasitas barang yang masuk adalah: {kapasitas_masuk} kg")
print(f"sisa Knapsack adalah: {kapasitas }kg")
print(f"total harga adalah: {hargatotal}")

