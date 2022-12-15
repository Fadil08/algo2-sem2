from tkinter import *
from math import *

wh = "1000x1000"
w = int(wh.split("x")[0])
h = int(wh.split("x")[1])
l = 10

program = Tk()
program.title("Connecting Graph")
cnv = Canvas(program, width=w, height=h)

points = []
total = int(input())
for i in range(total):
    line = input()
    x = int(line.split(" ")[0])
    y = int(line.split(" ")[1])
    points.append((x, y))

i = 0
while i <= len(points):
    i += 1
    j = 0
    while j <= len(points):
        if j + 1 < len(points):
            if points[j][1] < points[j + 1][1]:
                points[j], points[j + 1] = points[j + 1], points[j]
            if points[j][1] == points[j + 1][1]:
                if points[j][0] > points[j + 1][0]:
                    points[j], points[j + 1] = points[j + 1], points[j]
        j += 1

j = 0
for i in points:
    cnv.create_oval(i[0], i[1], i[0]+l, i[1]+l, fill="red")
    cnv.create_text(i[0], i[1], text=str((i[0], i[1])))
    j += 1

for i in range(len(points)):
    if i + 1 < len(points):
        cnv.create_line(points[i][0]+l/2, points[i][1]+l/2, points[i + 1][0]+l/2, points[i + 1][1]+l/2, fill="blue")

cnv.pack()
program.mainloop()