import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=1500, height=1500)
canvas.pack()

# mengelola input nodes
total_node = int(input())
node_list = []
for i in range(total_node):
    nodes = input()
    v1 = int(nodes.split()[0])
    v2 = int(nodes.split()[1])
    node_list.append([v1, v2])
    # menggambar node
    canvas.create_oval(v1-10, v2-10, v1+10, v2+10, fill="green")
    canvas.create_text(v1, v2, text=str(i), fill="white")

# mengelola input edges
total_edge = int(input())
edge_list = {}
# mengolah dictionary yang terdapat key awal berupa titik 0 lalu valuenya adalah key pasangan node yang valuenya adalah bobot
for i in range(total_edge):
    edges = input()
    node_x = int(edges.split()[0])
    node_y = int(edges.split()[1])
    weight = int(edges.split()[2])
    if node_x not in edge_list:
        edge_list[node_x] = {}
    edge_list[node_x][node_y] = weight
    if node_y not in edge_list:
        edge_list[node_y] = {}
    edge_list[node_y][node_x] = weight
        
# mengelola input start node dan finish node
inputan = input()
start = int(inputan.split()[0])
finish = int(inputan.split()[1])

# DEBUGGING
# print(edge_list)
# mencari semua kemungkinan jalur
def cari_jalur(graf, awal, akhir, jalur=[]):
    jalur = jalur + [awal]
    if awal == akhir:
        return [jalur]
    if awal not in graf:
        return []
    semua_jalur = []
    for node in graf[awal]:
        if node not in jalur:
            jalur_baru = cari_jalur(graf, node, akhir, jalur)
            for jalur_baru_ in jalur_baru:
                semua_jalur.append(jalur_baru_)
    return semua_jalur


# menghitung jarak semua jalur
jalur = cari_jalur(edge_list, start, finish)
# dari hasil dari cari_jalur, total bobot dari semua nilai pada array di jalur tersebut dan diappend ke dalam jalur
for i in jalur:
    cost = 0
    # menghitung total bobot dari semua nilai pada array di jalur tersebut dan nilainya ditambahkan pada masing-masing array
    for j in range(len(i)-1):
        cost += edge_list[i[j]][i[j+1]]
    i.append(cost)
    # print(i)

# print(jalur)
jalur = sorted(jalur, key=lambda x: x[-1])
print("Jalur terpendek:", jalur[0][:-1], "dengan total cost:", jalur[0][-1])
# menghapus costnya
for i in jalur:
    i.pop()

# merubah indeks ke node
for i in range(len(jalur)):
    for j in range(len(jalur[i])):
        jalur[i][j] = node_list[jalur[i][j]]


result = jalur[0]
# menggambar semua jalur
for i in range(len(jalur)):
    for j in range(len(jalur[i])-1):
        canvas.create_line(jalur[i][j][0], jalur[i][j][1], jalur[i][j+1][0], jalur[i][j+1][1], fill="red")
    

# menggambar jalur result
for i in range(len(result)-1):
    canvas.create_line(result[i][0], result[i][1], result[i+1][0], result[i+1][1], fill="blue")


window.mainloop()