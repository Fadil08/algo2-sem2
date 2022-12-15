print('\t-->Program ke I<--')
kalimat =input ('masukkan kalimat: ')

jumlah_spasi = 0
jumlah_vocal = 0
jumlah_konsonan = 0

huruf_vocal= ['a,i,u,e,o,A,I,U,E,O']

for i in kalimat:
    if i.isspace():
        jumlah_spasi+=1
    elif i in ['a','i','u','e','o','A','I','U','E','O']:
        jumlah_vocal+=1
    else:
         jumlah_konsonan+=1

print ('Jumlah Dari Huruf vocal adalah: ',jumlah_vocal)
print ('Jumlah Dari Huruf Konsonan adalah: ',jumlah_konsonan)
print ('Jumlah Dari Huruf Spasi adalah: ',jumlah_spasi)