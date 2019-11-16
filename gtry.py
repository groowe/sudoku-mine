# tryout of logic
import tkinter as tk
import tkinter.font as font

win = tk.Tk()

selectednumber = None
oldnumber = None
def key(event):
    try:
        global selectednumber
        if 0 < int(event.char) < 10:
            selectednumber = int(event.char)
            print(f"selectednumber = {selectednumber}")
            showgrid3()
    except:
        return

mainframe = tk.Frame(win,width=160,height=160)

mainframe.bind("<Key>",key)
mainframe.focus()
mainframe.pack()    
#print("mf packed")
def tryout(x,y):

    global grid
    change = False
    if selectednumber != None:
        if str(selectednumber) in grid[x][y]:
            grid[x][y] = selectednumber
            change = True
    if change:
#        cleanup(grid)
        showgrid3(x,y)

grid = [["123456789" for i in range(2)] for i in range(2)]

butgrid = [[None for i in range(2)] for i in range(2)]


def showgrid3(ex=None,ey=None):
    
    dark = ["01","10"]
    global butgrid
    global grid
    if not (ex == ey == None):
        x = ex
        y = ey
        f = butgrid[ex][ey][0]
        b = butgrid[ex][ey][1]
        xy = str(ex)+str(ey)
        if xy in dark:
            bg = "light blue"
            activebackground = bg
        else:
            bg = "grey"
            activebackground = bg
        text = grid[x][y]
        print(text)
 
        fg = "black"
        if type(grid[x][y]) == int:
            state="disabled"
            myfont = font.Font(size=30,weight="bold")
        else:
            state="active"
            myfont = font.Font(size=10)
#        b = tk.Button(f,text=text,state=state,fg=fg,font=myfont,bg=bg,activebackground=bg)
        b["text"] = text
        b["state"] = state
        b["fg"] = fg
        b["font"] = myfont
        b["bg"] = bg
        b["activebackground"] = bg
#        b["command"] = lambda ix = x, iy = y : tryout(ix,iy)
#        b.grid(sticky ="NWSE")
#        b.bind("<Key>",key)
#        b.bind("<Button-1>",lambda *args : tryout)
#        b.focus_set()
#        b.bind("<Button-3>",lambda *args , ex = x , ey = y : clear(*args,ex,ey))
        butgrid[x][y] = f,b
        return


    for x in range(2):
        for y in range(2):
            xy = str(x)+str(y)
            if xy in dark:
                bg = "light blue"
                activebackground = bg
            else:
                bg = "grey"
                activebackground = bg
            f = tk.Frame(mainframe,width=80,height=80)
            text = grid[x][y]
            print(text)

            fg = "black"
            if type(grid[x][y]) == int:
                state="disabled"
                myfont = font.Font(size=30,weight="bold")
            else:
                state="active"
                myfont = font.Font(size=10)
            b = tk.Button(f,text=text,state=state,fg=fg,font=myfont,bg=bg,activebackground=bg)
            b["command"] = lambda ix = x, iy = y : tryout(ix,iy)
            f.rowconfigure(0,weight=1)
            f.columnconfigure(0,weight=1)
            f.grid_propagate(0)
            f.grid(row = x , column = y)
            b.grid(sticky ="NWSE")
            b.bind("<Key>",key)
            b.bind("<Button-1>",lambda *args : tryout)
            b.focus_set()
            b.bind("<Button-3>",lambda *args , ex = x , ey = y : clear(*args,ex,ey))
            butgrid[x][y] = f,b
    print(butgrid)

def clear(event,x,y):
    global grid
    change = False
    if type(grid[x][y]) == int:
        return
    if selectednumber != None:
        if str(selectednumber) in str(grid[x][y]):
            if len(str(grid[x][y])) > 1:
                grid[x][y] = grid[x][y].replace(str(selectednumber),"")
                change = True
    if change:
        showgrid3(x,y)


if __name__ == "__main__":
    showgrid3()
    
    
    
    win.mainloop()
