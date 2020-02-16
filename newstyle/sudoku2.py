from grid import basicgrid,standardize,done,validate_solution,copyofgrid
from grid import easy , medium , hard , extreme , hardest , hardest2
from grid import hardestinvalid , extremeinvalid
from grid import preprint , printgrid
from level0 import Cleanup,Naked_Single,Unique
from level1 import Naked_Pair,Hidden_Pair,Box_Line,Pointing_Line
from level2 import Naked_Multiple,Hidden_Multiple,Lines_2,NT,NT_chains,Y_Wing
# level3 isn't working yet .. !!!

#### this part is needed only until generator doesn't work
fullsdks = []
def sudoku17():
    import random
    global fullsdks
    if not fullsdks:
        # this is link from
        # http://staffhome.ecm.uwa.edu.au/~00013890/sudokumin.php
        url = 'http://staffhome.ecm.uwa.edu.au/~00013890/sudoku17'
        fn = 'sudoku17'
        try:
            with open(fn,'r') as f:
                sdks = f.readlines()
        except FileNotFoundError:
            import subprocess
            t = subprocess.call(['wget',url])
            try:
                with open(fn,'r') as f:
                    sdks = f.readlines()

            except FileNotFoundError:
                print(f'please download file from {url} when available')

                print('http://staffhome.ecm.uwa.edu.au/~00013890/sudokumin.php')
                return basicgrid()
        for s in range(len(sdks)):
            sdks[s] = sdks[s].replace('\n','')
        fullsdks = [[] for i in sdks]
        for i in range(len(fullsdks)):
        #    while len(fullsdks[i]) < 10:
        #        fullsdks[i].append([])
             start = 0
             end = 9
             while end <= len(sdks[i]):

                 fullsdks[i].append([])
                 fullsdks[i][-1] = sdks[i][start:end]
                 start=end
                 end+=9
    ran = random.randint(0,len(fullsdks))
    return standardize(fullsdks[ran])


    for s in range(len(fullsdks)):
        print(fullsdks[s])
        print(sdks[s])
        print(standardize(fullsdks[s]))

###############################################################
import tkinter as tk
from tkinter import ttk , Menu
import tkinter.font as font
from tkinter.messagebox import showinfo

win = tk.Tk()

win.title('Sudoku')

selectednumber = None
oldnumber = None
grid =[ ['123456789' for i in range(9)] for i in range(9)]


def cleanup(gridd,ingame=False):
    cp = copyofgrid(gridd)
    c = Cleanup(gridd)
    if c[1]:
        diff = []
        for x in range(9):
            for y in range(9):
                if cp[x][y] != gridd[x][y]:
                    diff.append([x,y])
        global grid
        grid = cp
        print(f'diff = {diff}')
        for d in diff:
            partgrid(d[0],d[1])
    return c

############ events ##############
def key(event):
    print('pressed',repr(event.char))
    try:
        global selectednumber
        global oldnumber

        print('pressed',repr(event.char))
        if 0 < int(event.char) < 10:
            selectednumber = int(event.char)
            if oldnumber != selectednumber:
                highlight()

                oldnumber = selectednumber
    except:
        print(f'selectednumber = {selectednumber}')
        print(f'{event.char}')
        return

def callback(event):
    print('clicked at',event.x,event.y)

def call(event):
    mainframe.focus_set()
    callback(event)

###################################
def highlight():
    global grid
    g = cleanup(grid)
    grid = g[0]
    global butgrid
    if selectednumber == None or selectednumber == oldnumber:
        print(f'highlight : selectednumber = {selectednumber}')
        return
    coords = []
    olds = []
    for x in range(9):
        for y in range(9):
            new = str(selectednumber) in str(grid[x][y])
            old = False
            if oldnumber != None:
                old = str(oldnumber) in str(grid[x][y])
            if new:
                coords.append([x,y])
            if old:
                olds.append([x,y])
    print(coords,old)
    for i in range(len(coords)):
        x = coords[i][0]
        y = coords[i][1]
        partgrid(x,y)
    for o in range(len(olds)):
        x = olds[o][0]
        y = olds[o][1]
        partgrid(x,y)

def tryout(x,y):
    global grid
    change = False
    if selectednumber != None:
        if type(grid[x][y]) == int:
            return
        if str(selectednumber) in grid[x][y]:
            grid[x][y] = selectednumber
            change = True
    if change:
        g = cleanup(grid)
        grid = g[0]
        partgrid(x,y)
        highlight()

# for some reason wont work:
#def partgrid(x,y,new=False):
#    global grid
#    global butgrid
#
#    dark = ['01','10','12','21']
#    modx = int(x/3)
#    mody = int(y/3)
#    xy = str(modx)+str(mody)
#
#    if xy in dark:
#        bg = 'light blue'
#        activebackground = 'light blue'
#    else:
#        bg = 'grey'
#        activebackground = 'grey'
#    if str(selectednumber) in str(grid[x][y]):
#        bg = 'light grey'
#        activebackground = 'light grey'
#        if len(str(grid[x][y])) == 1:
#            activebackground = 'grey'
#            bg = 'grey'
#
#    text = str(grid[x][y])
#    state = 'active'
#    fg = 'black'
#    smallfont = font.Font(size=10)
#    bigfont = font.Font(size=30,weight='bold')
#    myfont = smallfont
#    if type(grid[x][y]) == int:
#        state = 'disabled'
#        fg = 'black'
#        myfont = bigfont
#    if new or butgrid[x][y] == None:
#        f = tk.Frame(mainframe,width=80,height=80)
#        f.rowconfigure(0,weight = 1)
#        f.columnconfigure(0,weight=1)
#        f.grid_propagate(0)
#        b = tk.Button(f,text=text,state=state,fg=fg,
#                bg=bg,activebackground=activebackground)
#        if type(grid[x][y]) == int:
#            b['font'] = bigfont
#        else:
#            b['font'] = smallfont
#
#    else:
#        f,b = butgrid[x][y]
#        if b['text'] !=str(grid[x][y]):
#            b['text'] = str(grid[x][y])
#        if type(grid[x][y]) == int:
#            b['font'] = bigfont
#            b['state'] = 'disabled'
#        else:
#            print('*')
#        if str(selectednumber) in str(grid[x][y]):
#            if type(grid[x][y]) != int:
#                b['bg'] = b['activebackground'] = '#B29700'
#            else:
#                b['bg'] = b['activebackground'] = '#CD853F'
#        else:
#            b['bg'] = b['activebackground'] = bg
#        return
#
#    f.grid(row=x,column =y)
#    b.grid(sticky = 'NWSE')
#    b.bind('<Key>',key)
#    b.bind('<Button-1>', lambda *args,ix=x, iy=y : tryout(ix,iy))
#    b.focus_set()
#    s = x
#    b.bind('<Button-3>',lambda *args,es = s,ey=y : clear(*args,es,ey))
#    butgrid[x][y] = f,b

def partgrid(x,y,new=False):
    global grid
    global butgrid
#   00 01 02
#   10 11 12
#   20 21 22
#    print(f"partgrid {x}{y}")
    dark = ["01","10","12","21"]
    modx = int(x/3)
    mody = int(y/3)
    xy = str(modx)+str(mody)

    if xy in dark:
#        bg="dark green"
        bg = "light blue"

        activebackground= "light blue"
    else:
#        bg="green"
        bg = "grey"
        activebackground = "grey"
#<<<<<<< HEAD
#=======
##### TO BE IMPLEMENTED .. but probably in a different way ###########
#>>>>>>> 909998e13b9b51e99c0b210a573be1582385e87a

    if str(selectednumber) in str(grid[x][y]):
        bg = "light grey"
        activebackground = "light grey"
        if len(str(grid[x][y])) == 1:
#            activebackground = 'FFD700'
#            bg = '#FFD700'
            activebackground = 'grey'
#            activebackground = '#FFD700'
            bg = 'grey'
#<<<<<<< HEAD
#=======
######################################################################
#>>>>>>> 909998e13b9b51e99c0b210a573be1582385e87a
    text = str(grid[x][y])
#    text = grid[x][y]
#    bg = butbg(x,y)
    state= "active"
    fg = "black"
    smallfont = font.Font(size=10)
    bigfont = font.Font(size=30,weight="bold")
    myfont = smallfont
    if type(grid[x][y]) == int:
        state="disabled"
        fg = "black"
        myfont = bigfont
    if new or butgrid[x][y] == None:
        f = tk.Frame(mainframe,width=80,height=80)
        f.rowconfigure(0,weight = 1)
        f.columnconfigure(0,weight = 1)
        f.grid_propagate(0)
        b = tk.Button(f,text=text,state=state,fg=fg,
                bg=bg,activebackground=activebackground)
        if type(grid[x][y]) == int:
            b["font"] = bigfont
        else:
            b["font"] = smallfont
    else:
        f,b = butgrid[x][y]
        if b["text"] != str(grid[x][y]):
            b["text"] = str(grid[x][y])
        if type(grid[x][y]) == int:
            b["font"] = bigfont
            b["state"] = "disabled"

#        else:
#            print("")
        if str(selectednumber) in str(grid[x][y]):
#<<<<<<< HEAD
            if type(grid[x][y]) != int:
#                b["bg"] = b["activebackground"] = "light grey"

                b["bg"] = b["activebackground"] = "#B29700"
#=======
#            b["bg"] = b["activebackground"] = "light grey"
            else:
                b["bg"] = b["activebackground"] = '#CD853F'
#>>>>>>> 909998e13b9b51e99c0b210a573be1582385e87a
        else:
            b["bg"] = b["activebackground"] = bg

        return


#        b.destroy()
#        b = tk.Button(f,text=text,state=state,fg=fg,
#                font=myfont,bg=bg,activebackground=activebackground)


#    b["command"] = lambda ix = x , iy = y : tryout(ix,iy)
#     b["text"] =  gridvalue(x,y)
#    print(f"{b['text']}")

#    print(f"a = <{x}>, b = <{y}>")
    f.grid(row = x,column = y)
    b.grid(sticky = "NWSE")
    b.bind("<Key>",key)
    b.bind("<Button-1>", lambda *args, ix=x, iy = y : tryout(ix,iy))
    b.focus_set()
    s = x
#      g = lambda ix = x , iy = y : clear(ix,iy)


    b.bind("<Button-3>", lambda *args , es = s, ey = y : clear(*args,es,ey))
    butgrid[x][y] = f,b




def _quit():
    raise SystemExit

def clear(event,x,y):
    global grid
    change = False
    print(f'xy = {x}{y} {grid[x][y]} seleced = {selectednumber}')
    if type(grid[x][y]) == int:
        return
    if selectednumber != None:
        if str(selectednumber) in str(grid[x][y]):
            if len(str(grid[x][y])) > 1:
                change = True
                grid[x][y] = grid[x][y].replace(str(selectednumber),'')
    if change:
        c =cleanup(grid)
        print(c[1])
        partgrid(x,y)

def mf():
    global mainframe
    global botbut
    global wf

    wf = tk.Frame(win,width=800,height=900)
    wf.pack()
    mainframe = tk.Frame(wf,width=800,height=800)
    mainframe.pack()
    botbut = tk.Frame(wf,width=800,height=100)
    botbut.pack()
    return True
mf()
def setgrid(st,name=''):
    global grid
    global gridlist
    global guessed
    guessed= 0
    gridlist = []
    butgrid =[ [None for i in range(9)] for i in range(9)]
    grid = st()
    showgrid3(new=True)
    printgrid(grid)
    tt= 'Sudoku '+name
    win.title(tt)


def maintwo():
    s = False
    while s != True:
        s = main()
    showgrid3(new=True)

def main():
    global grid
    global guesed
    completed,valid = done(grid)
    print(completed,valid)
    while not (completed and valid):
        progress = solve()
        completed,valid = done(grid)

def solve():
    global grid
    print(f'grid = {grid[0]}')
    func =[ [Cleanup,Naked_Single,Unique],
            [Naked_Pair,Hidden_Pair,Box_Line,Pointing_Line],
            [Naked_Multiple,Hidden_Multiple,Lines_2,Y_Wing]
            ]

    # unit === Unique,Naked_Pair,Hidden_Pair,Naked_Multiple
    # Hidden_Multiple
    neededunit =[ [False,False,True],
            [True,True,False,False],
            [True,True,False,False]
            ]
    found = False
    for level in range(len(func)):
        for f in range(len(func[level])):
            if neededunit[level][f]:
                for x in range(9):
                    r = func[level][f](grid[x]) # row
                    if r[1]:
                        found = True
                        grid[x] =r[0]
                    c = [] # column
                    for s in range(9):
                        c.append(grid[s][x])
                    c = func[level][f](c)
                    if c[1]:
                        found = True
                        for s in range(9):
                            grid[s][x] = c[0][s]
                # sqr
                for modx in range(3):
                    for mody in range(3):
                        sqr = []
                        for x in range(modx*3,(modx+1)*3):
                            for y in range(mody*3,(mody+1)*3):
                                sqr.append(grid[x][y])
                        sqr = func[level][f](sqr)
                        if sqr[1]:
                            found = True
                            ind = 0
                            for x in range(modx*3,(modx+1)*3):
                                for y in range(mody*3,(mody+1)*3):
                                    grid[x][y] = sqr[0][ind]
                                    ind+=1
            else:
                g = func[level][f](grid)
                if g[1]:
                    found = True
                    grid = g[0]
        if found:
            return True
    return found




    

def showgrid3(x= None, y= None, new=False):
    global grid
    global butgrid

    if type(x) == type(y) == int:
        if 0 <= x <9 and 0<=y<9:
            partgrid(x,y,new)
    else:
        for x in range(9):
            for y in range(9):
                partgrid(x,y,new)


        

if __name__ == '__main__':

    menuBar = Menu(win)
    win.config(menu=menuBar)

    butgrid = [[None for i in range(9)] for i in range(9)]
    #gridbar = Menu(win)
    #win.config(menu=gridbar)

    gridbar = Menu(menuBar,tearoff=0)
    #win.config(menu=gridbar)

    gridbar.add_command(label="easy",command=lambda * args: setgrid(easy,"easy"))
    gridbar.add_command(label="medium",command=lambda * args: setgrid(medium,"medium"))
    gridbar.add_command(label="hard",command=lambda * args: setgrid(hard,"hard"))
    gridbar.add_command(label="extreme",command=lambda * args: setgrid(extreme,"extreme"))
    gridbar.add_command(label="hardest",command=lambda * args: setgrid(hardest,"hardest"))
    gridbar.add_command(label="hardest2",command=lambda * args: setgrid(hardest2,"hardest2"))
    gridbar.add_command(label="impos1",command=lambda * args: setgrid(impos1,"impos1"))
    gridbar.add_command(label="impos2",command=lambda * args: setgrid(impos2,"impos2"))
    gridbar.add_command(label="impos3",command=lambda * args: setgrid(impos3,"impos3"))
    gridbar.add_command(label="sudoku17",command=lambda * args: setgrid(sudoku17,"sudoku17"))
    gridbar.add_command(label="hardestinvalid",command=lambda * args: setgrid(hardestinvalid,"hardestinvalid"))
    gridbar.add_command(label="extremeinvalid",command=lambda * args: setgrid(extremeinvalid,"extremeinvalid"))
    gridbar.add_command(label="custom",command=lambda * args: setgrid(emptygrid,"custom"))
    menuBar.add_cascade(label="set",menu=gridbar)


    fileMenu = Menu(menuBar,tearoff=0)
    fileMenu.add_command(label="exit",command=exit)
    fileMenu.add_command(labe="solve",command=maintwo)
    menuBar.add_cascade(label="File",menu=fileMenu)

    win.mainloop()

