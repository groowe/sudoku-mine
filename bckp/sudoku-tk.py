# gui for sudoku
# in tk
from sudoku import *
import tkinter as tk
from tkinter import ttk , scrolledtext , Menu

win = tk.Tk()

win.title("Sudoku")

#aLabel = ttk.Label(win, text="A Label")
#aLabel.grid(column=0, row=0)

for i in range(1,10):
    s = "Button"+str(i)
    a = i
    if i > 3:
        a+=1
        if i > 6:
            a+=1
    s = tk.Button(win,text=str(i),width=3,height=3)
    s.grid(column=str(a),row=3)
#    print(s)
### temp  -- needed grid definition
#grid = [[None for i in range(9)] for i in range(9)]
### / temp


def showgrid():
    global grid
    for a in range(9):
        for b in range(9):
            x = str(a)+str(b)
            if type(grid[a][b]) == int:
                text = str(grid[a][b])
            else:
                text = ""
    
#                text = str(grid[a][b])
            x = tk.Button(win,text=text,width=3,height=3)
            c = b
            if b > 2:
                c+=1
                if b > 5:
                    c+=1
            d = a
            if a > 2:
                d+=1
                if a > 5:
                    d+=1

 
            x.grid(column=str(c+1),row=str(d+5))

def exit():
    raise SystemExit()
    quit()

#grid = impos2()

def maintwo():
    s= main()
    while s != True:
        s = main()

#    if main() == True:
    showgrid()

def setgrid():
    global grid
    grid = hard()
    showgrid()


showgrid()
menuBar = Menu(win)
win.config(menu=menuBar)

#gridbar = Menu(win)
#win.config(menu=gridbar)

gridbar = Menu(menuBar,tearoff=0)
#win.config(menu=gridbar)
gridbar.add_command(label="easy",command=setgrid)
gridbar.add_command(label="medium",command=setgrid)
gridbar.add_command(label="hard",command=setgrid)

menuBar.add_cascade(label="set",menu=gridbar)

fileMenu = Menu(menuBar,tearoff=0)
fileMenu.add_command(label="exit",command=exit)
fileMenu.add_command(labe="solve",command=maintwo)
menuBar.add_cascade(label="File",menu=fileMenu)

#gridlist = []
#guessed = 0
win.mainloop()
