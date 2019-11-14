import tkinter as tk
win = tk.Tk()

win.title("Sudoku")

def emptygrid():
    return [["123456789" for i in range(9)] for i in range(9)]

grid = emptygrid()

def showgrid():
    global grid
    for a in range(9):
        for b in range(9):
            x = str(a)+str(b)
            if type(grid[a][b]) == int:
                text = str(grid[a][b])
            else:
                text = grid[a][b]
            x = tk.Button(win,text=text,width=3,height=3)
            x.grid(column=str(b),row=str(a))
            print(f"{a} {b}")

showgrid()

# RUN
win.mainloop()
