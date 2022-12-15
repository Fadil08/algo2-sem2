import tkinter as tk



ukuran = input()
ukuran = ukuran.split(" ")
X = int(ukuran[0])
Y = int(ukuran[1])

panjang = 50
Y1 = 50
peta = []
# X1 = 50
# X2 = 50
# cnv.create_rectangle(50, 50, 100, 100, fill='#cbcbcb')
# cnv.create_rectangle(350, 350, 100, 100)
for i in range(Y):
    baris = input()
    # X2 = 50
    peta2 = []
    for j in range(X):
        # warna = 'red'
        if baris[j] == '0':
            # warna = 'white'
            peta2.append(0)
        else:
            peta2.append(1)
        # cnv.create_rectangle(X2, Y1, X2 + panjang, Y1 + panjang, fill=warna)
        # X2 += panjang
    # Y1 += panjang
    peta.append(peta2)

# print(peta)

X_pos = input()
Y_pos = input()

X_pos = X_pos.split(' ')
X_pos = [int(X_pos[0]), int(X_pos[1])]
Y_pos = Y_pos.split(' ')
Y_pos = [int(Y_pos[0]), int(Y_pos[1])]


# X_pos = (1,1)
# Y_pos = (9,9)

def ke_atas():
    X_pos[1] -= 1
def ke_bawah():
    X_pos[1] += 1
def ke_kanan():
    X_pos[0] += 1
def ke_kiri():
    X_pos[0] -= 1

while True:
    # x, y = X_pos
    x = X_pos[0]
    y = X_pos[1]
    if Y_pos[0] == x and Y_pos[1] == y:
        break

    # apakah bisa ke atas?
    if peta[y-1][x] == 0:
        # lakukan gerak ke atas
        ke_kanan()
    # apakah bisa ke bawah
    elif peta[y+1][x] == 0:
        # lakukan gerak ke bawah
        ke_bawah()
    # apakah bisa ke kanan
    elif peta[y][x+1] == 0:
        # lakukan gerak ke kanan
        ke_kanan()
    # apakah bisa ke kiri
    elif peta[y][x-1] == 0:
        ke_kiri()

window = tk.Tk()
window.title('pertemuan 10')

cnv = tk.Canvas(window, width=1000, height=600)
cnv.pack()

window.mainloop()