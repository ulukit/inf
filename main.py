import tkinter as tk

file = open('data.txt', 'r')
lines = file.read().splitlines()
values = [list(map(int,element.split())) for element in lines]

root = tk.Tk()
canvas = tk.Canvas(width=300, height=300)

o = 65
for i in values:
    canvas.create_oval(i[0]-3, i[1]-3, i[0]+3, i[1]+3, fill='black')
    canvas.create_text(i[0]-7, i[1]-7, text=chr(o))
    o += 1

current = 1

def click(e):
    global current
    if abs(e.x-values[current][0]) <= 6 and abs(e.y-values[current][1]) <= 6:
        canvas.create_line(values[current-1][0],values[current-1][1],values[current][0],values[current][1])
        current += 1
    else:
        print('wrong')

canvas.pack()
root.bind('<Button-1>',click)
root.mainloop()