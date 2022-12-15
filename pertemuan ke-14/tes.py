import tkinter as tk
import copy

window = tk.Tk()
cnv = tk.Canvas(window, width=1280, height=1000)
cnv.pack()

def inputTitik(n):
    setTitik = []
    for i in range(n):
        titikSet = input()
        x= int(titikSet.split(' ')[0])
        y= int(titikSet.split(' ')[1])
        cnv.create_oval(x-10,y+10,x+10,y-10,fill='green')
        cnv.create_text(x,y,text=i, font = 8, fill='white')
        setTitik.append([x,y])
   
    return setTitik

def inputTargetAwal(titik):
    target = input()
    awal = int(target.split(' ')[0])
    akhir = int(target.split(' ')[1])

    return [titik[awal], titik[akhir]]

def setConnect(TiTik):
    set = []
    n = int(input())
    for i in range(n):
        setInput = input()
        titik1 = int(setInput.split(' ')[0])
        titik2 = int(setInput.split(' ')[1])
        bobot = int(setInput.split(' ')[2])

        set.append([TiTik[titik1], TiTik[titik2], bobot])
        cnv.create_line(TiTik[titik1], TiTik[titik2])
        cnv.create_text((TiTik[titik1][0]+TiTik[titik2][0])/2,(TiTik[titik1][1]+TiTik[titik2][1])/2, text=bobot, font=10 )

    return set

def setTitikTetangga(set, pos, titikSet):
    titikTetangga = []
    setOfSet = copy.deepcopy(set)
    titiKK = copy.deepcopy(titikSet)
    for set in setOfSet:
        if (pos == set[0] or pos == set[1]):
            set.remove(pos)
            if set[0] not in titiKK:
                titikTetangga.append(set)

    return titikTetangga

def coloum(list2d, extractColom):
    object = []
    for set in list2d:
        object.append(set[extractColom])

    return sum(object)

def pathShort(set_path):
    pathOfpath = []
    for i in set_path:
        pathOfpath.append(coloum(i, 2))
    minimal_path = min(pathOfpath)

    return set_path[pathOfpath.index(minimal_path)]

def Path(set, pos, TargetTitik, walk=[], titikSet=[]):
    setTetangga = setTitikTetangga(set, pos, titikSet)
    if len(setTetangga) == 0:
        return None

    for tetangga in setTetangga:
        if tetangga[0] == TargetTitik:
            walk.append([pos, tetangga[0], tetangga[1]])
            path.append(copy.deepcopy(walk))
            walk.pop()
            return None
        else:
            titikSet.append(pos)
            walk.append([pos, tetangga[0], tetangga[1]])
            Path(set, tetangga[0], TargetTitik, walk, titikSet)
            titikSet.pop()
            walk.pop()

nTitik = int(input())
titik = inputTitik(nTitik)
set = setConnect(titik)

ChooseTitik = inputTargetAwal(titik)
titikawal = ChooseTitik[0]
titiktarget = ChooseTitik[1]

path = []
Path(set, titikawal, titiktarget)

shortestPath = pathShort(path)

for set in shortestPath:
    cnv.create_line(set[0], set[1], fill='yellow', width=3)
    
window.mainloop()