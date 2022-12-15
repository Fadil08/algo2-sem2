import tkinter as tk

window = tk.Tk()
window.title('Labirin')
canvas = tk.Canvas(window, height=1000, width=1000)
canvas.pack()

inputan = input()
panjang_baris = int(inputan.split(' ')[0])
lebar_baris = int(inputan.split(' ')[1])

hasil_maze = []
# mengumpulkan array ke dalam hasil_maze
for i in range(lebar_baris):
    baris = input()
    maze_temp = []
    for j in range(panjang_baris):
        if baris[j] == '0':
            maze_temp.append(0)
        else:
            maze_temp.append(1)
    hasil_maze.append(maze_temp)

# menyusun hasil_maze menjadi struktur labirin
def create_maze(maze):
    for i in maze:
        for j in i:
            print(j, end='')
        print()

def mazeSolver(maze, currentPosition, finishPosition):
    current_y, current_x = currentPosition
    finish_x, finish_y = finishPosition
    # kotak pertama diberi nomor 2
    maze[current_y][current_x] = 2

    # cek jalur atas
    if maze[current_y-1][current_x] == 0:
        # jika jalur atas sudah buntu dan harus kembali
        mustReturn = mazeSolver(maze, [current_y-1, current_x], finishPosition)
        if mustReturn:
            return True
    elif maze[current_y-1][current_x] == maze[finish_y][finish_x]:
        maze[current_y][current_x] = 4
        return True
    
    # cek jalur bawah
    if maze[current_y+1][current_x] == 0:
        # jika jalur bawah sudah buntu dan harus kembali
        mustReturn = mazeSolver(maze, [current_y+1, current_x], finishPosition)
        if mustReturn:
            return True
    elif maze[current_y+1][current_x] == maze[finish_y][finish_x]:
        maze[current_y][current_x] = 4
        return True

    # cek jalur kiri
    if maze[current_y][current_x-1] == 0:
        # jika jalur kiri sudah buntu dan harus kembali
        mustReturn = mazeSolver(maze, [current_y, current_x-1], finishPosition)
        if mustReturn:
            return True
    elif maze[current_y][current_x-1] == maze[finish_y][finish_x]:
        maze[current_y][current_x] = 4
        return True    
        

    # cek jalur kanan
    if maze[current_y][current_x+1] == 0:
        mustReturn = mazeSolver(maze, [current_y, current_x+1], finishPosition)
        if mustReturn:
            return True
    elif maze[current_y][current_x+1] == maze[finish_y][finish_x]:
        maze[current_y][current_x] = 4
        return True


    maze[current_y][current_x] = 3

# letak robot
robot_position = input()
robot_position = int(robot_position.split(' ')[1]), int(robot_position.split(' ')[0])

# letak objek
object_position = input()
object_position = int(object_position.split(' ')[0]), int(object_position.split(' ')[1])

print(mazeSolver(hasil_maze, robot_position, object_position))
create_maze(hasil_maze)

# menggambar di tkinter berdasarkan hasil_maze yang baru
for i in range(lebar_baris):
    for j in range(panjang_baris):
        if hasil_maze[i][j] == 0:
            canvas.create_text(j*50+25, i*50+25, text='0', fill='white')
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill='white')
        elif hasil_maze[i][j] == 1:
            canvas.create_text(j*50+25, i*50+25, text='0', fill='white')
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill='grey')
        elif hasil_maze[i][j] == 2:
            canvas.create_text(j*50+25, i*50+25, text='0', fill='white')
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill='yellow')
        elif hasil_maze[i][j] == 3:
            canvas.create_text(j*50+25, i*50+25, text='0', fill='white')
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill='red')
        elif hasil_maze[i][j] == 4:
            canvas.create_text(j*50+25, i*50+25, text='0', fill='white')
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill='green')

window.mainloop()