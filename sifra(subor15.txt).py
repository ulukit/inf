import re
import tkinter as tk

file = open(file='subor15.txt')
rawlines = file.readlines()
lines = [x[:-1] for x in rawlines]

root = tk.Tk()
canvas = tk.Canvas(height = 300, width = 300)

for line in lines:
    rawtype = re.search('[A-Z]',line)
    type = rawtype.group()
    coord = re.findall('[0-9]+', line)
    if type == 'K':
        x,y,off = int(coord[0]),int(coord[1]),int(coord[2])
        canvas.create_oval(x-off,y-off,x+off,y+off)
    elif type == 'S':
        x,y,off = int(coord[0]),int(coord[1]),int(coord[2])
        canvas.create_rectangle(x,y,x+off,y+off)
    elif type == 'U':
        x,y,x1,y1 = int(coord[0]),int(coord[1]),int(coord[2]),int(coord[3])
        canvas.create_line(x,y,x1,y1)

canvas.pack()
root.mainloop()
