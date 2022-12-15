print('---> Menghitung Jmmlah Huruf Vokal, Huruf Konsonan, dan Karakter Spasi')
kalimat = input("Masukkan Sebuah Kalimat : ")

JumlahVokal = 0
JumlahKonsonan = 0
KarakterSpasi = 0
for i in kalimat :
    if i in ['a','i','u','e','o','A','I','U','E','O']:
        JumlahVokal +=1
    elif i == ' ':
        KarakterSpasi +=1
    else:
        JumlahKonsonan +=1

print('Jumlah Huruf Vokal Kalimat Tersebut = ',JumlahVokal)
print('Jumlah Huruf Konsonan Kalimat Tersebut = ',JumlahKonsonan)
print('Jumlah Karakter Spasi Kalimat Tersebut = ',KarakterSpasi)