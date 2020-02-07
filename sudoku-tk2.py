#!/usr/bin/env python   

# sudoku
# source of ideas :
# https://www.rharriso.com/generating-sudoku-boards-pt-1-structures.html?source=post_page---------------------------

#One effective strategy is to look at each cell in turn and then try to eliminate possible numbers. The more neighbors (which I define as cells that are in the same row, column, or block) that a cell has filled in the fewer possibility options that cell has. If a cell only has one valid possible move, is can be filled. As cells get filled it’s neighbors get fewer and fewer options, and more cells can be filled.

#More difficult puzzles require a bit more work as there aren’t enough cells filled in for this simple method.


# naive way :
#####
#Rough Naive Algorithm 

# Start at first cell
# Pick a value that isn’t present in any neighbors
# If at last cell, exit
# Otherwise go to next cell
# Go to step 2

# this py is solving it by trying some logic (enough most of the times)
# if not solved by logic,( guess  + logic) untill solved
# standalone naive way is done by solve_by_guess()
# logic (one step) is done by solve()
# naive way (one step) is done by guessing()
# combination of it is done by main() # obviously


#define grid

fn = 'sudoku17'
fullsdks = []
def sudoku17():
    import random
    global fullsdks
    if not fullsdks:
        with open(fn,'r') as f:
            sdks = f.readlines()
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


def easy():
    grid = basicgrid()
    grid[0] = [0,3,0,8,1,0,7,0,6]
    grid[1] = [6,0,1,7,9,5,0,3,8]
    grid[2] = [0,0,7,3,0,6,0,0,5]
    grid[3] = [0,7,8,5,0,0,0,0,1]
    grid[4] = [0,0,6,4,0,7,3,0,0]
    grid[5] = [3,0,0,0,0,9,8,6,0]
    grid[6] = [4,0,0,6,0,8,5,0,0]
    grid[7] = [8,6,0,9,3,4,1,0,2]
    grid[8] = [7,0,3,0,5,1,0,8,0]
    grid = standardize(grid)
#    print("whoooo")
    return grid

def medium():
    grid = basicgrid()
    grid[0] = [1,0,0,2,0,6,9,0,0]
    grid[1] = [0,5,0,0,3,0,2,0,0]
    grid[2] = [0,0,0,7,0,9,0,6,0]
    grid[3] = [9,0,0,0,0,0,8,4,5]
    grid[4] = [5,0,0,0,0,0,0,0,7]
    grid[5] = [2,8,4,0,0,0,0,0,6]
    grid[6] = [0,1,0,6,0,7,0,0,0]
    grid[7] = [0,0,2,0,1,0,0,5,0]
    grid[8] = [0,0,6,8,0,5,0,0,9]
    grid = standardize(grid)
    return grid

def hard():
    grid = basicgrid()
    grid[0] = [3,0,1,4,0,0,0,0,0]
    grid[1] = [9,0,0,0,0,0,6,2,7]
    grid[2] = [0,0,0,9,0,8,0,0,4]
    grid[3] = [0,0,0,0,0,0,1,7,2]
    grid[4] = [0,3,0,0,6,0,0,9,0]
    grid[5] = [1,2,9,0,0,0,0,0,0]
    grid[6] = [6,0,0,3,0,9,0,0,0]
    grid[7] = [7,9,5,0,0,0,0,0,1]
    grid[8] = [0,0,0,0,0,7,9,0,6]
    return standardize(grid)


def extreme():
    grid = basicgrid()
    grid[0] = [4,3,0,0,0,0,0,0,0]
    grid[1] = [6,0,0,0,0,0,0,2,5]
    grid[2] = [2,0,0,0,3,8,0,0,0]
    grid[3] = [0,0,4,0,5,0,0,1,0]
    grid[4] = [0,0,5,8,0,9,6,0,0]
    grid[5] = [0,9,0,0,1,0,5,0,0]
    grid[6] = [0,0,0,1,9,0,0,0,6]
    grid[7] = [3,7,0,0,0,0,0,0,9]
    grid[8] = [0,0,0,0,0,0,0,3,1]
    return standardize(grid)
#    grid[0] = []




def hardest():

    grid = basicgrid()
    grid[0] = [8,0,0,0,0,0,0,0,0]
    grid[1] = [0,0,3,6,0,0,0,0,0]
    grid[2] = [0,7,0,0,9,0,2,0,0]
    grid[3] = [0,5,0,0,0,7,0,0,0]
    grid[4] = [0,0,0,0,4,5,7,0,0]
    grid[5] = [0,0,0,1,0,0,0,3,0]
    grid[6] = [0,0,1,0,0,0,0,6,8]
    grid[7] = [0,0,8,5,0,0,0,1,0]
    grid[8] = [0,9,0,0,0,0,4,0,0]
    return standardize(grid)

def hardest2():
    grid = basicgrid()
    grid[0] = [1,0,0,0,0,7,0,9,0]
    grid[1] = [0,3,0,0,2,0,0,0,8]
    grid[2] = [0,0,9,6,0,0,5,0,0]
    grid[3] = [0,0,5,3,0,0,9,0,0]
    grid[4] = [0,1,0,0,8,0,0,0,2]
    grid[5] = [6,0,0,0,0,4,0,0,0]
    grid[6] = [3,0,0,0,0,0,0,1,0]
    grid[7] = [0,4,0,0,0,0,0,0,7]
    grid[8] = [0,0,7,0,0,0,3,0,0]
    return standardize(grid)

def hardestinvalid():
    grid  = hardest()
    grid[8][8] = 3
    return grid


def basicgrid():

    return [[None for i in range(9)] for i in range(9)]

def standardize(grid):
    gg = []
    for x in range(len(grid)):
        gg.append([])
        for y in range(len(grid[x])):
            gg[x].append([])
            if grid[x][y] == None or grid[x][y] == 0 or grid[x][y] == '0':
#                grid[x][y] == "123456789"
                gg[x][y] = '123456789'
            else:
                gg[x][y] = int(grid[x][y])
    return cleanup(gg)


# clean from impossible numbers
def cleanup(grid,ingame=False):
    change = False
    changes = []
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == int:
                modx = int(x/3)
                mody = int(y/3)
                num = str(grid[x][y])
                for ix in range(9):
                    for iy in range(9):
                        if type(grid[ix][iy]) == str:
                            modix = int(ix/3)
                            modiy = int(iy/3)
                            inrow = (x == ix)
                            incul = (y == iy)
                            numing = (num in grid[ix][iy])
                            diff = not (inrow and incul)
                            insqr = ((modx == modix) and (mody == modiy))
                            if diff and (inrow or incul or insqr) and numing:
                                grid[ix][iy] = grid[ix][iy].replace(num,"")
                                change = True
                                changes.append([ix,iy])
    if change and ingame:
#        showgrid3()
        for c in changes:
            partgrid(c[0],c[1],new=False)
#                                if ingame:
#                                    showgrid3(ix,iy)
    return grid

# clean print
def preprint(line):
#    s = []
#    for item in line:
#        if type(item) == int:
#            s.append(item)
#        else:
#            s.append(" ")
#    s = [" " if type(x) == int else x for x in line]
#    s = [if type(x) == int x for x else " " for x in line]
    s = [i if type(i) == int else " " for i in line]
    s = str(s)
    s = s.replace("None"," ").replace("[","|")
    s = s.replace("]","|").replace("\'","")

    line = s
    newline = ""
    countchar = 0
    checkchar = ","
    for char in line:
        if char == checkchar:
            countchar +=1
            if countchar % 3 == 0:
                newline +='|'
            else:
                newline +=' '
        else:
            newline+=char
    return newline


def printgrid(clean = True):
    global grid
    if clean == False:
        for x in range(len(grid)):
            print(grid[x])
        return
    print("_"*27)
    for x in range(len(grid)):
#       # print('x')
#       # print(x)
        if x > 0 and x % 3 == 0:
            print("_"*27)
        s = preprint(grid[x])
#        print(len(s))
        print("{}".format(s))
    print("_"*27)


def done():
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) != int:
                return False , False
    return True , validate_solution()


def validate_solution():
    nums = [i for i in range(1,10)]
    for num in nums:
        count = 0
        for x in range(9):
            for y in range(9):
                if grid[x][y] == num:
                    count+=1
        if count != 9:
            print(f"{num} == {count}")
            return False
    return True

def copygrid(fromgrid = None):
    if fromgrid == None:
        global grid
        fromgrid = grid
    bckp = basicgrid()
    nums = [i for i in range(1,10)]
    for num in nums:
        for x in range(9):
            for y in range(9):
                if fromgrid[x][y] == num:
                    bckp[x][y] = num
    bckp = standardize(bckp)
    return cleanup(bckp)

     



def guess():
    guesses = []
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                guess = [x,y,int(grid[x][y][0]),grid[x][y][1:]]
                guesses.append([len(grid[x][y]),guess])
#               # print("guessing : ")
#               # print(f"{guess}")
#               # input()
    guesses.sort()
    guess = guesses[0][1]
    return guess
#    printgrid(False)

def showguesses():
    if len(gridlist) > 0:
        for g in gridlist:
            s = g[-1]
            print(s)
#        input()

def possible():
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                if len(grid[x][y]) == 0:
                   # print("not possible :")
                   # print(x,y,grid[x][y])
#                    printgrid(False)
                    return False
    nums = [i for i in range(1,10)]
    for num in nums:
        count = 0
        for x in range(9):
            for y in range(9):
                if grid[x][y] == num:
                    count+=1
        if count > 9:
            return False
    return True


def solve_by_guess():
    global gridlist
    global grid
    solved ,valid = done()
#   # print("step 1")
    printgrid()
    while not solved:
#        showguesses()

#        printgrid()
        solved,valid = done()
#       # print("step 2")
#       # print(solved,valid)
#       # print("lengrid = {}".format(len(gridlist)))
        if solved == False and valid == False :
            cell = guess()
           # print("newguess")
           # print(cell)
            gridlist.append([copygrid(),cell])
            grid[cell[0]][cell[1]] = int(cell[2])
#           # print(cell)
#           # print(grid[cell[0]][cell[1]])
            grid = cleanup(grid)
#            printgrid()
#           # input()
#           # print("step 3")
#       # print(possible())
        if not possible():
#           # print("step 4")
#           # print("gridlist -1 1 = {}".format(gridlist[-1][1]))
#           # input()
            value = gridlist[-1][1][3]
            while len(value) == 0:
                if len(gridlist) > 2:
                    x1 = gridlist[-1][-1][0]
                    y1 = gridlist[-1][-1][1]
                    x2 = gridlist[-2][-1][0]
                    y2 = gridlist[-2][-1][1]
#                    print(x1,y1)
#                    print(x2,y2)
#                    input()
                    if x1 == x2 and y1 == y2:
#                        print(x1,y1)
#                        print(x2,y2)
                        invalid = str(gridlist[-1][1][2])
                        gridlist[-2][-1][3] = gridlist[-2][-1][3].replace(invalid,"")

#                print(len(gridlist))
                gridlist = gridlist[:-1]

#               # print(len(gridlist))
                value = gridlist[-1][1][3]
#               # print(f"value = {value}")
#           # print("step 5")
#           # print(gridlist[-1][0])
            grid = copygrid(gridlist[-1][0])
            cell = gridlist[-1][1]
           # print(f" cell = {cell}")
            x = cell[0]
            y = cell[1]
            value = cell[3]
 #          # print("step 6")
 #          # print("x {}  y {} value {}".format(x,y,value))
 #          # print(type(x))
 #          # print(type(y))
 #          # print(type(value))
            grid[x][y] = value
#            print(x,y,value)
#            print(grid[x][y])
#            printgrid()
#        input()
#        printgrid(False)
       # input()
 #          # print("step 7")
 #          # print(len(gridlist))
 #          # input()
    printgrid()
    print(validate_solution())


def newgrid():
    temp = [ ["123456789" for i in range(9)] for i in range(9)]
    for i in range(9):
        temp[i][i] = i+1
    temp = cleanup(temp)
    return temp
            
def extremeinvalid():
    grid = extreme()
    grid[4][4] = 6
    return grid




def row():
    progress = False
    for x in range(9):
        row = grid[x]
        for i in range(len(row)):
            if type(row[i]) == int:
                num = row[i]
                for a in range(len(row)):
                    if i != a :
                        if type(row[a]) == str:
                            grid[x][a] = grid[x][a].replace(str(num),"")
                            if len(grid[x][a]) == 1:

                                doit = setnum(grid[x][a],x,a)
                                if doit == True:
                                    progress = True


        if progress == False:
            for i in range(len(row)):
                if type(row[i]) == str:
                    nums = row[i]
                    for num in nums:
                        unique = True
                        for a in range(len(row)):
                            if a != i:
                                if type(row[a]) == str:
                                    if num in row[a]:
                                        unique = False
                        if unique == True:
                            doit = setnum(num,x,i)
                            if doit == True:
                                progress = True
                                row = []
                                for xs in range(9):
                                    row.append(grid[x][xs])



    return progress

def culomn():
    progress = False
    for y in range(9):
        cul = []
        for x in range(9):
            cul.append(grid[x][y])
        for i in range(len(cul)):
            if type(cul[i]) == int:
                num = str(cul[i])
                for a in range(len(cul)):
                    if i != a:
                        if type(cul[a]) == str:
                            grid[a][y] = grid[a][y].replace(num,"")
                            if len(grid[a][y]) == 1:

                                doit = setnum(grid[a][y],a,y)
                                if doit == True:
                                    progress = True

                            cul[a] = grid[a][y]

        if progress == False:
            for i in range(len(cul)):
                if type(cul[i]) == str:
                    nums = cul[i]
                    for num in nums:
                        unique = True
                        for a in range(len(cul)):
                            if a != i:
                                if type(cul[a]) == str:
                                    if num in cul[a]:
                                        unique = False
                        if unique == True:
                            doit = setnum(num,i,y)
                            if doit == True:
                                progress = True
                                cul = []
                                for xs in range(9):
                                    cul.append(grid[xs][y])
    return progress

def sqr():
    progress = False
    modx =0
    mody =0
    while modx < 3:
        square = []
        for x in range(modx*3,(modx*3)+3):
            for y in range(mody*3,(mody*3)+3):
                square.append(grid[x][y])
        for cell in range(len(square)):
            if type(square[cell]) == int:
                num = str(square[cell])
                for i in range(len(square)):
                    if i != cell:
                        if type(square[i]) == str:
                            xi = int(i/3) # 0 0 0 1 1 1 2 2 2  = x in grid
                            yi = int(i%3) # 0 1 2 0 1 2 0 1 2  = y in grid
                            x = modx*3 + xi
                            y = mody*3 +yi
                            grid[x][y] = grid[x][y].replace(num,"")
                            if len(grid[x][y]) == 1:
                                doit = setnum(grid[x][y],x,y)
#                                grid[x][y] = int(grid[x][y])
                                if doit == True:
                                    progress = True
                            square[i] = grid[x][y]
        if progress == False:
            for i in range(len(square)):
                if type(square[i]) == str:
                    nums = square[i]
                    for num in nums:
                        unique = True
                        for a in range(len(square)):
                            if a != i:
                                if type(square[a]) == str:
                                    if num in square[a]:
                                        unique = False
                        if unique == True:
                            xi = int(i/3) # 0 0 0 1 1 1 2 2 2  = x in grid
                            yi = int(i%3) # 0 1 2 0 1 2 0 1 2  = y in grid
                            x = modx*3 + xi
                            y = mody*3 +yi
                            doit = setnum(grid[x][y],x,y)
                            if doit == True:
                                progress = True
                                isquare = []
                                for x in range(modx*3,(modx*3)+3):
                                    for y in range(mody*3,(mody*3)+3):
                                        square.append(grid[x][y])
        if mody == 2:
            modx += 1
            mody = 0
        else:
            mody += 1
    return progress



def neigh():
    progress = False
    for x in range(9):
        modx = int(x/3)
        for y in range(9):
            mody = int(y/3)
            if type(grid[x][y]) == int:
                num = str(grid[x][y])
                for xs in range(9):
                    modxs = int(xs/3)
                    for ys in range(9):
                        modys = int(ys/3)
                        typ = (type(grid[xs][ys]) == str)
                        inrow = (x == xs)
                        incul = (y == ys)
                        diff = not (inrow and incul)
                        insqr =( (modx == modxs) and (mody == modys))
                        if diff and typ and (inrow or incul or insqr):
                            grid[xs][ys] = grid[xs][ys].replace(num,"")
                            if len(grid[xs][ys]) == 1:
                                grid[xs][ys] = int(grid[xs][ys])
                                progress = True

    return progress


def solve():
    r = row()
    c = culomn()
    s = sqr()
    n = neigh()
    return (r or s or c or n)



def setnum(num,x,y,step = 0):
    if type(num) != int:
        num = int(num)
        if num > 9 or 1 > num:
            return False
    modx = int(x/3)
    mody = int(y/3)
    for ix in range(9):
        modix = int(ix/3)
        for iy in range(9):
            modiy = int(iy/3)
            inrow = (x == ix)
            incul = (y == iy)
            diff = not (inrow and incul)
            insqr = ((modx == modix) and (mody == modiy))
            if step == 0:
                typ =  (type(grid[ix][iy]) == int)
            else:
                typ =  (type(grid[ix][iy]) == str)
            if diff and typ and (incul or inrow or insqr):
                if step == 0 and grid[ix][iy] == num:
                    return False
                if step == 1:
                    grid[ix][iy] = grid[ix][iy].replace(str(num),"")
    if step == 0:
        return setnum(num,x,y,1)
    grid[x][y] = num
    return True


def guessing(poss = None):
    global grid
    global gridlist
    if poss == None:
        poss = possible()
#    print(f"poss = {poss}")
#    print(f"len gridlist = {len(gridlist)}")
    if not poss:
        if len(gridlist) == 0:
            print("invalid puzzle")
#            quit()
        try:
            value = gridlist[-1][1][3]
        except IndexError:
            tk.messagebox.askokcancel('popup','invalid puzzle!')
            hardest()
            return False

        while len(value) == 0:
            if len(gridlist) > 1:
                x1 = gridlist[-1][-1][0]
                y1 = gridlist[-1][-1][1]
                x2 = gridlist[-2][-1][0]
                y2 = gridlist[-2][-1][1]
                if x1 == x2 and y1 == y2:
                    invalid = str(gridlist[-1][1][2])
                    gridlist[-2][-1][3] = gridlist[-2][-1][3].replace(invalid,"")
            gridlist = gridlist[:-1]
            try:
                value = gridlist[-1][1][3]
            except IndexError:
                tk.messagebox.askokcancel('popup','invalid puzzle!')
                hardest()
                return False
            print("value = {value}")
        grid = copygrid(gridlist[-1][0])
        cell = gridlist[-1][1]
        x = cell[0]
        y = cell[1]
        cell[2] = cell[3][0]
        cell[3] = cell[3][1:]
        value = cell[2]
        gridlist[-1][1] = cell
        grid[x][y] = value
    else:
        cell = guess()
        gridlist.append([copygrid(),cell])
        x = cell[0]
        y = cell[1]
        num = cell[2]
#        grid[x][y] = num
        grid = cleanup(grid)
        grid[x][y] = num

def main():
    global guessed
    printgrid()
    completed , valid = done()
    print(completed,valid)
    while not (completed and valid):
        progress = solve()
        completed,valid = done()


        print(completed,valid)
        print(progress)
#        printgrid()
        if not progress:
            printgrid()
            guessed +=1
            printgrid(False)
            if guessing(possible()) == False:
                completed,valid= True,True
#                hardest()


            showguesses()
            print(len(gridlist))
#            input()
#            quit()
#            input()
#        quit()
    printgrid()
    print(guessed)
    return True

    print(validate_solution())

def impos1():
    grid = basicgrid()
    grid[0] = [0,0,0,0,0,0,6,0,9]
    grid[1] = [0,0,0,0,0,1,0,8,2]
    grid[2] = [4,8,0,0,0,0,7,0,0]
    grid[3] = [0,0,0,5,0,7,0,0,8]
    grid[4] = [0,0,0,0,0,9,0,1,6]
    grid[5] = [0,3,0,2,0,0,0,0,0]
    grid[6] = [0,0,0,0,5,0,0,0,7]
    grid[7] = [0,0,3,4,0,0,0,0,0]
    grid[8] = [0,0,6,0,0,0,0,4,0]
    grid = standardize(grid)
    return grid

def empty():
    grid = basicgrid()
    grid[0] = [0,0,0,0,0,0,0,0,0]
    grid[1] = [0,0,0,0,0,0,0,0,0]
    grid[2] = [0,0,0,0,0,0,0,0,0]
    grid[3] = [0,0,0,0,0,0,0,0,0]
    grid[4] = [0,0,0,0,0,0,0,0,0]
    grid[5] = [0,0,0,0,0,0,0,0,0]
    grid[6] = [0,0,0,0,0,0,0,0,0]
    grid[7] = [0,0,0,0,0,0,0,0,0]
    grid[8] = [0,0,0,0,0,0,0,0,0]
    grid = standardize(grid)
    return grid

def impos2():
    grid = basicgrid()
    grid[0] = [0,0,0,1,0,0,6,0,8]
    grid[1] = [0,1,4,0,0,0,5,0,0]
    grid[2] = [0,0,8,0,5,7,0,0,0]
    grid[3] = [0,0,6,0,0,0,0,4,0]
    grid[4] = [0,4,2,0,0,0,0,9,0]
    grid[5] = [0,0,0,2,0,5,0,0,0]
    grid[6] = [0,0,7,0,0,0,3,0,0]
    grid[7] = [0,0,0,0,8,2,0,0,0]
    grid[8] = [0,0,9,0,0,3,0,0,0]
    grid = standardize(grid)
    return grid

def impos3():
    grid = basicgrid()
    grid[0] = [0,0,0,0,5,7,0,0,1]
    grid[1] = [0,0,0,6,0,0,9,0,0]
    grid[2] = [0,0,0,0,0,0,5,4,3]
    grid[3] = [0,0,0,9,2,0,0,0,4]
    grid[4] = [0,3,0,0,0,1,0,0,6]
    grid[5] = [0,2,0,0,0,0,0,0,8]
    grid[6] = [0,0,0,0,7,0,0,0,5]
    grid[7] = [0,0,0,3,0,0,4,0,0]
    grid[8] = [2,0,0,0,0,0,0,8,0]
    grid = standardize(grid)
    print("impos3 whohooo")
    return grid


def emptygrid():
    return [["123456789" for i in range(9)] for i in range(9)]

grid = emptygrid()

gridlist = []
guessed = 0

#############################################
  ################ GUI PART ###############
#############################################
import tkinter as tk
from tkinter import ttk , Menu
import tkinter.font as font
from tkinter.messagebox import showinfo
win = tk.Tk()

win.title("Sudoku")
#win.rowconfigure(1)
#win.columnconfigure(2)

selectednumber = None
oldnumber = None

##<<<<<<< HEAD
#
#
##=======
##>>>>>>> 909998e13b9b51e99c0b210a573be1582385e87a
def highlight():
    global butgrid
    if selectednumber == None or selectednumber == oldnumber:
        return
    coords = []
    olds = []
    print(selectednumber,oldnumber)
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
#        d = butgrid(cor[0],cor[1][1])
#        d["bg"] = "grey"
#        d["activebackground"] = "grey"
        x = coords[i][0]
        y = coords[i][1]
        print(x,y)
        partgrid(x,y)
    for o in range(len(olds)):
        x = olds[o][0]
        y = olds[o][1]
        print(x,y)
        partgrid(x,y)


def key(event):
    try:

        global selectednumber
        global oldnumber

#<<<<<<< HEAD
#        print("pressed", repr(event.char))
#=======
        print("pressed", repr(event.char))
#>>>>>>> 909998e13b9b51e99c0b210a573be1582385e87a
        if 0 < int(event.char) < 10:
            selectednumber = int(event.char)
            if oldnumber != selectednumber:
                highlight()

                oldnumber = selectednumber
    except:
#        print(f"selectednumber = {selectednumber}")
#        print(f"{event.char}")
        return
    print(selectednumber)

def callback(event):
#    mainframe.focus_set()
#    print(f"{x}{y}")
    print("clicked at",event.x, event.y)

def call(event):
    mainframe.focus_set()
    callback(event)
def mf():
    global mainframe
    global botbut
    global wf
        
    wf = tk.Frame(win,width = 800 ,height = 900)
    wf.pack()
    mainframe = tk.Frame(wf,width=800,height=800)#.grid(row=0,column=0)
    mainframe.pack()
    botbut = tk.Frame(wf,width=800,height=100)#.grid(row=0,column=1)
    
#    leftbut.grid(row=0,column=1)
    botbut.pack()
    return True

def recount():
    rcount = [None,0,0,0,0,0,0,0,0,0]
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == int:
                rcount[grid[x][y]]+=1

    return rcount

def printnum():
    global botbut
#    global 
    counts = recount()
    for x in range(1,10):
        count = counts[x]
        num = x



#def leftbut():
    

def tryout(x,y):
    global grid
#    print(f"{x}{y} = {grid[x][y]}")
    change = False
    if selectednumber != None:
        if type(grid[x][y]) == int:
            return

        if str(selectednumber) in grid[x][y]:
            grid[x][y] = selectednumber
            change = True
    if change:
        grid = cleanup(grid,True)
        partgrid(x,y)
        highlight()
#        showgrid3()
mf()


def showgrid3(x= None, y = None,new = False):
    global butgrid    
    global grid
#    s = mf()
    for x in range(9):
        for y in range(9):
            partgrid(x,y,new)

#            g = lambda sx = x , iy = y : clear(sx,iy) 
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

        else:
            print("")
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
#    print(f"{x}{y} {grid[x][y]} {selectednumber}")
    print(str(selectednumber) in grid[x][y])
    if type(grid[x][y]) == int:
        return
    if selectednumber != None:
        if str(selectednumber) in str(grid[x][y]):
            if len(str(grid[x][y])) > 1:
                grid[x][y] = grid[x][y].replace(str(selectednumber),"")
                change = True
#                print(f"change = {change}")
    if change:
        partgrid(x,y)



def maintwo():
    s= main()
    while s != True:
        s = main()

    showgrid3(new=True)


def setgrid(st,name = ""):
    global grid
    global gridlist
    global guessed
    guessed = 0
    gridlist = []
    butgrid = [[None for i in range(9)] for i in range(9)]
    grid = st()
#    showgrid()
#    showgrid2()
    showgrid3(new=True)
    printgrid()
    tt = "Sudoku "+name
    win.title(tt)
    print(st)
    print(grid)
#    input()

if __name__ == "__main__":
#    showgrid()
##    showgrid2()
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

