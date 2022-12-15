import tkinter as tk


window = tk.Tk()
cnv = tk.Canvas(window, width=1000, height=1000)
cnv.pack()


luasMaze = input()
tinggi = int(luasMaze.split(' ')[0])
lebar = int(luasMaze.split(' ')[1])

peta = []
for _ in range(tinggi):
    baris = input()
    x = 0
    kotak = []
    for kolom in range(0, lebar):
        kotak.append(int(baris[kolom]))
    peta.append(kotak)

robot = input().split(' ')
robot[0] = int(robot[0])
robot[1] = int(robot[1])
finish = input().split(' ')
finish[0] = int(finish[0])
finish[1] = int(finish[1])

print('Posisi awal ',robot)
print('Target ',finish)
peta[robot[1]][robot[0]] = 7
peta[finish[1]][finish[0]] = 5

current = robot
def keAtas():
    current[1]=current[1]-1

def keKanan():
    current[0]=current[0]+1

def keBawah():
    current[1]=current[1]+1

def keKiri():
    current[0]=current[0]-1

def tandaiSudahLewat():
    peta[current_y][current_x] = 2    

def tandaiJalanBuntu():
    peta[current_y][current_x] = 3

for i in range(len(peta)):
    print(peta[i])
print('')

while True:     
    current_x = current[0]
    current_y = current[1]
    if (peta[current_y-1][current_x] == 5):
        tandaiSudahLewat()
        keAtas()
        peta[current_y-1][current_x] = 2
        break
    elif (peta[current_y][current_x+1] == 5):
        tandaiSudahLewat()
        keKanan()
        peta[current_y][current_x+1] = 2
        break
    elif (peta[current_y+1][current_x] == 5):
        tandaiSudahLewat()
        keBawah()
        peta[current_y+1][current_x] = 2
        break
    elif (peta[current_y][current_x-1] == 5):
        tandaiSudahLewat()
        keKiri()  
        peta[current_y][current_x-1] = 2
        break

    elif (peta[current_y-1][current_x] == 0):
        tandaiSudahLewat()
        keAtas()
    elif (peta[current_y][current_x+1] == 0):
        tandaiSudahLewat()
        keKanan()
    elif (peta[current_y+1][current_x] == 0):
        tandaiSudahLewat()
        keBawah()
    elif (peta[current_y][current_x-1] == 0):
        tandaiSudahLewat()
        keKiri()
    
    elif (peta[current_y-1][current_x] == 2):
        tandaiJalanBuntu()
        keAtas()   
    elif (peta[current_y][current_x+1] == 2):
        tandaiJalanBuntu()
        keKanan()
    elif (peta[current_y+1][current_x] == 2):
        tandaiJalanBuntu()
        keBawah()
    elif (peta[current_y][current_x-1] == 2):
        tandaiJalanBuntu()
        keKiri()
        
y = 0
sisi = 50
for baris in range(tinggi):
    x = 0
    for kolom in range(0, lebar):
        if peta[baris][kolom] == 1:
            cnv.create_rectangle(x,y,x+sisi,y+sisi,fill = 'red')
        elif peta[baris][kolom] == 0:
            cnv.create_rectangle(x,y,x+sisi,y+sisi,fill = 'white')
        elif peta[baris][kolom] == 2:
            cnv.create_rectangle(x,y,x+sisi,y+sisi,fill = 'yellow')
        elif peta[baris][kolom] == 3:
            cnv.create_rectangle(x,y,x+sisi,y+sisi,fill = 'black')
        x+=50   
    y += 50

window.mainloop()