import tkinter
main = tkinter.Tk()
c = tkinter.Canvas(height = 600, width = 600)
rows = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for a in range(2):
    c.create_line((a+1)*200,0,(a+1)*200,600)
    c.create_line(0,(a+1)*200,600,(a+1)*200)

sus1 = tkinter.PhotoImage(file = 'sus1.png')
sus2 = tkinter.PhotoImage(file = 'sus2.png')
victory = tkinter.PhotoImage(file = 'victory.png')
def click(event):
    x, y = event.x, event.y
    if event.num == 1:
        rows[y//200][x//200] = 1
        c.create_image((x//200*200)+100, (y//200*200)+100, image = sus1)
        if win(1) == 1:
            c.create_image(300,300, image = victory)
    if event.num == 3:
        rows[y//200][x//200] = 2
        c.create_image((x//200*200)+100, (y//200*200)+100, image = sus2)
        if win(2) == 1:
            c.create_image(300,300, image = victory)
    print(rows)

def column(matrix, i):
    return [row[i] for row in matrix]

def win(r):
    for a in range(3):
        if rows[a] == [r,r,r]:
            state = 1
            return(state)
        elif column(rows,a) == [r,r,r]:
            state = 1
            return (state)


c.bind_all('<Button-1>', click)
c.bind_all('<Button-3>', click)
c.pack()
main.mainloop()