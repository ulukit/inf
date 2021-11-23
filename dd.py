import tkinter as tk
import random as rand

window = tk.Tk

canvas = tk.Canvas(width=1020, height=70)
canvas.pack()

stv=[]

for i in range(20):
    r = (rand.randint(0, 255))
    g = (rand.randint(0, 255))
    b = (rand.randint(0, 255))
    color = "#%02x%02x%02x" % (r, g, b)
    print(color)
    canvas.create_rectangle(15 + (i * 50), 15, 55 + (i * 50), 55, fill=color)
    stv.append(15 + (i * 50))
print(stv)
print(120//65)


def klik1(event):
    x = ((event.x-15)//50)+1
    if event.x in range ((x*50+5)-40, (x*50+5)) and event.y in range(15,55):
        canvas.coords(x, 10 + ((x-1) * 50), 10, 60 + ((x-1) * 50), 60)
    print(event.x)
    print(x)

def klik2(event):
    x = ((event.x-15)//50)+1
    if event.x in range ((x*50+5)-40, (x*50+5)) and event.y in range(15,55):
        canvas.coords(x, 15 + ((x-1) * 50), 15, 55 + ((x-1) * 50), 55)
    print(event.x)
    print(x)

canvas.bind("<Button-1>", klik1)
canvas.bind("<Button-3>", klik2)
canvas.mainloop()