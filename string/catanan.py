import collections
string=input('masukkan: ')
li=string.split(' ')
ambil=collections.Counter(li).most_common()

for kata in ambil:
    print(kata)