print ('\t Program perhitungan angka,kata,upper dan lower ')

angka = 0
kata = 0
upper = 0
lower = 0
kalimat = input ('-->masukkan kalimat<--: ')
hasil = ' '.join(filter(str.isalnum,kalimat))
kata_jabar= kalimat.split()



for i in hasil:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        angka+=1
    # elif i in kata_jabar:
    #     kata+=1
    

print ("jumlah huruf kata: ",len(kata_jabar))
print ("jumlah huruf besar: ",upper)
print ("jumlah huruf kecil: ",lower)
print ("jumlah huruf angka: ",angka)