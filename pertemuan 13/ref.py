import math
import tkinter as tk

window = tk.Tk()

def inptitik(n):
    case_titik = []
    for noUrut in range(n):
        titik = input()
        x= int(titik.split(' ')[0])
        y= int(titik.split(' ')[1])
        cnv.create_oval(x-10,y+10,x+10,y-10,fill='green')
        cnv.create_text(x,y,text=noUrut)
        case_titik.append([x,y])
   
    return case_titik

def jarak(titik1,titik2):
    result = math.sqrt(math.pow(titik1[0]-titik2[0],2) + math.pow(titik1[1]-titik2[1],2))
    return result

def min2d (list2d,extractIndex):
    lengthSet = []
    for index in list2d:
        lengthSet.append( (index[extractIndex]) )
    minimum = min(lengthSet)
    for i in list2d:
        if i[extractIndex] == minimum:
            return i 


def MinSpanningTree (case):
    titik =[]
    cnVertikal = [case[0]] #permulaan titik pertama
    discnVertikal = case[1:] #sisanya disconnected akan tersimpan disini
    #[ [V1,V2,length] ] titik
    x = len(case)-1
    while x > 0:
        temp1_titik = []
        for cnver in cnVertikal: #cn = connected
            temp2_titik = []            
            
            for dcver in discnVertikal : #dc = disconnected
                length = jarak(cnver, dcver)
                temp2_titik.append([cnver, dcver, length])
            
            # mencari jarak terdekat dari kombinasi cnver 
            mintitik = min2d(temp2_titik,2) 
            temp1_titik.append(mintitik)

        #memilih jarak terdekat diantara titik lainnya
        short_titik = min2d(temp1_titik,2)
        #extract ver yg dc dari list, index dc = 1
        shortestver = short_titik[1]

        #memindahkan titik yg dc menjadi cn
        cnVertikal.append(shortestver)
        discnVertikal.remove(shortestver)
        
        titik.append(min2d(temp1_titik,2))
    
        x-=1 
    return titik
        

cnv = tk.Canvas(window, height=1300, width=1300)
cnv.pack()
x = int(input())

case = inptitik(x)
titik = MinSpanningTree(case) 

for i in range(len(titik)):
    cnv.create_text((titik[i][0][0]+titik[i][1][0])/2,(titik[i][0][1]+titik[i][1][1])/2, text=i+1)
    cnv.create_line(titik[i][0],titik[i][1])

    
window.mainloop()



#[ ['2',5],['3',2],['x',9],[23,10]  ], 1  => return ['3',2]

#vertices   [v1 , v2 , v3 , v4] 2d        
#ver     [x , y ] 1d
#titik       [v1,v2,length] 2d
#titik set   [e1, e2, e3, e4] 3d