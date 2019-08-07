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
    return grid
def basicgrid():

    return [[None for i in range(9)] for i in range(9)]
global grid
grid = []
def standardize(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                grid[x][y] = None
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

def printgrid():
    print("_"*27)
    for x in range(len(grid)):
#        print('x')
#        print(x)
        if x > 0 and x % 3 == 0:
            print("_"*27)
        s = preprint(grid[x])
#        print(len(s))
        print("{}".format(s))
    print("_"*27)



def done():
    for x in range(9):
        for y in range(9):
#            print(type(grid[x][y]),x,y,grid[x][y])
            if grid[x][y] == None or grid[x][y] == 0:
#                print(x,y)
                return False
            if type(grid[x][y]) == str:

#                print(x,y)
                return False
#    print("huh?")
    return isvalid()



def initial_solve():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == None or grid[x][y] == 0:
                grid[x][y] = "123456789"
    printgrid()

#    #input("initialsolve")
    isvalid()
    printgrid()
#    #input("aftersolve")



def finalcheck(num,x,y):
    if type(num) == str:
        num = int(num)
    if not ( 0 < num <= 9):
        return False
    divx = int(x/3)
    divy = int(y/3)
    for ex in range(9):
        divex = int(ex/3)
        for ey in range(9):
            divey = int(ey/3)
            insqr = ((divx == divex) and (divy == divey))
            inrow = (y == ey)
            incul = (x == ex)
            difstr = not((x == ex) and (y == ey)) 
            if difstr and (insqr or inrow or incul):
                if grid[ex][ey] == num:
                    print(num,x,y,ex,ey)
                    return False
    return True


def sqr3():
    modx =0
    mody = 0 # sqr by sqr
    while modx < 3:
        sqr = []
        for ex in range(modx*3,(modx*3)+3):
            for ey in range(mody*3,(mody*3)+3):
                sqr.append(grid[ex][ey])
#        print(sqr,modx,mody)
#        printgrid()
#        #input()

        for i in range(9): # go through full sqr
            rownum = int(i/3) # add to modx*3 to get x coord in grid
            culnum = i % 3  # add to mody*3 to get y coord in grid
#            print(rownum,culnum)
#            print(f'modx = {modx},mody = {mody}')
            six = (modx*3) + rownum
#            print(six,type(six))
            siy = (mody*3) + culnum
#            print(siy,type(siy))
#            print(f'sqr{i} = {sqr[i]}')
#            print(f'grid[{six}][{siy}] = {grid[six][siy]}')
#            if sqr[i] == grid[rownum+(modx*3)][culnum+(mody*3)]:
#                print(True)
#                #input()
#            else:
#                print(False)
#                printgrid()
#                #input("ERRRRRRRRRRRRR")
            if type(sqr[i]) == str:
                for num in sqr[i]: # for every number in cell
                    uniqueinrow = True
                        
                    uniqueincul = True
                    for a in range(9): # go through full sqr
#                        print(f'num = {num},a = {a}')

                        rowa = int(a/3)
                        cula = a % 3
                        if type(sqr[a]) == str and a != i:
#                            print(sqr[a],rowa,rownum,cula,culnum)
                            if num in sqr[a]:
#                                print(f'sqr[{a}] = {sqr[a]}')
                                if rowa != rownum:
                                    uniqueinrow = False
#                                else:

#                                    print(f'cula = {cula},culnum = {culnum}')
                                if cula != culnum:
                                    uniqueincul = False
                        
                    x = rownum + (modx*3)
                    y = culnum + (mody*3)
#                    print(f'num = {num}, x,y = {x},{y}\nrowunique = {uniqueinrow},culunique = {uniqueincul}')
                    if uniqueinrow or uniqueincul:
#                        print(sqr)
                        printgrid()
#                        #input()

                    if uniqueinrow == True:
                        for sy in range(9):
                            modsy = int(sy/3)
                            if modsy != mody:
                                if type(grid[x][sy]) == str:
                                    grid[x][sy] = grid[x][sy].replace(num,"")
                                    if len(grid[x][sy]) == 1:

                                        grid[x][sy] = int(grid[x][sy])
                                        #clearnei(grid[x][sy],x,sy)
                                        if not isvalid():
                                            guess(False)
                                        return sqr3()
                    elif uniqueincul == True:
                        for sx in range(9):
                            modsx = int(sx/3)
                            if modsx != modx:
                                if type(grid[sx][y]) == str:
                                    grid[sx][y] = grid[sx][y].replace(num,"")

                                    if len(grid[sx][y]) == 1:
                                        grid[sx][y] = int(grid[sx][y])
                                        if not isvalid():
                                            guess(False)
                                        #clearnei(grid[sx][y],sx,y)
                                        return sqr3()



        if mody ==2:
            mody = 0
            modx +=1
        else:
            mody +=1
#        print(modx,mody)
#        print("sqr")
#        printgrid()
#        #input()


def isvalid():
    allint = True
    for x in range(9):
        modx = int(x/3)
        for y in range(9):
            mody = int(y/3)
            if type(grid[x][y]) == int:
                num = grid[x][y]
                for ex in range(9):
                    modex = int(ex/3)
                    for ey in range(9):
                        modey = int(ey/3)
                        insqr = ((modx == modex) and (mody == modey))
                        inrow = (x == ex)
                        incul = (ey == y)
                        diff = not (inrow and incul)
                        if diff and (insqr or inrow or incul):
                            if type(grid[ex][ey]) == int:
                                if grid[ex][ey] == grid[x][y]:
                                    return False
                            if type(grid[ex][ey]) == str:
                                allint = False
                                if len(grid[ex][ey]) == 0:
                                    return False
                                if str(num) in grid[ex][ey]:
                                    if len(grid[ex][ey]) == 1:
                                        return False
                                    grid[ex][ey] = grid[ex][ey].replace(str(num),"")

                                    return isvalid()
                                    grid[ex][ey] = int(grid[ex][ey])
                                    #if len(grid[ex][ey]) == 1:
                                    #    grid[ex][ey] = int(grid[ex][ey])
    if allint == True:
        printgrid()
        print("solved")
        print(len(gridlist))
        print(failed)
        quit()
    return True


def row():
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                for n in grid[x][y]:
                    un = True
                    for i in range(9):
                        if i != y:
                            if type(grid[x][i]) == str:
                                if n in grid[x][i]:
                                    un = False
                            if type(grid[x][i]) == int:
                                if int(n) == grid[x][i]:
                                    if type(grid[x][y]) == str:
                                        grid[x][y] = grid[x][y].replace(n,"")
                                        un = False
                    if un == True:
                        if type(grid[x][y]) == str:

                            grid[x][y] = int(n)
                            if not isvalid():
                                guess(False)
                            #clearnei(int(n),x,y)



def cul():
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                for n in grid[x][y]:
                    un = True
                    for ex in range(9):
                        if ex != x:
                            if type(grid[ex][y]) == str:
                                if n in grid[ex][y]:
                                    un = False
                            if type(grid[ex][y]) == int:
                                if int(n) == grid[ex][y]:
                                    if type(grid[x][y]) == int:
                                        printgrid()
                                        #input()
                                        un = False
                                    else:
                                        grid[x][y] = grid[x][y].replace(n,"")
                    if un == True:
                        grid[x][y] = int(n)
                        #clearnei(int(n),x,y)
                        if not isvalid():
                            guess(False)



def solvesqr2(sqr):
    # if n numbers are in n cells, no other number can be in those cells
    listnums = []
    for i in range(9):
        if type(sqr[i]) == str:
            for number in sqr[i]:
                alreadydone = False
                for item in listnums:
                    if item[0] == number:
                        alreadydone = True

                if alreadydone == False:

                    num = [number,[i],1]
                    for a in range(9):
                        if i != a:
                            if type(sqr[a]) == str:
                                if number in sqr[a]:
                                    num[1].append(a)
                                    num[2]+=1
                    listnums.append(num)


#    if len(listnums) > 2:
#
#        print(listnums)
#        #input()
    for item in listnums:
        numberiter = [item[0]]
        a = item[1]
        for atem in listnums:
            if atem[1] is not a:
                if atem[1] == a:
                    numberiter.append(atem[0])
        if len(numberiter) > 1:
            if len(numberiter) == len(a):
                print(numberiter,a)
                numbersnow = ""
                for n in numberiter:
                    numbersnow+=n
                for index in a:
                    sqr[index] = numbersnow
                for i in range(9):
                    if type(sqr) == str:
                        if i not in a:
                            for snum in numberiter:
                                sqr[i] = sqr[i].replace(snum,"")
#                return solvesqr2(sqr,modx,mody)
    return sqr

def solveit():
    cul()
    row()
    sqr3()
    sqr4()



def sqr4():
    modx = 0
    mody = 0 # same system as sqr3
    while modx < 3:
        sqr = []
        for x in range(modx*3,(modx*3)+3):
            for y in range(mody*3,(mody*3)+3):
                sqr.append(grid[x][y])
        sqrnow = solvesqr2(sqr)
        if sqrnow != sqr:
            index= 0
            for x in range(modx*3,(modx*3)+3):
                for y in range(mody*3,(mody*3)+3):
                    grid[x][y] = sqr[index]




        if mody == 2:
            mody = 0
            modx +=1
        else:
            mody +=1
    for rowx in range(9):
        s = grid[rowx]
        t = solvesqr2(s)
        if s != t:
            print()
            grid[rowx] = t
        
    for sy in range(9):
        cul = []
        for sx in range(9):
            cul.append(grid[sx][sy])

        newcul = solvesqr2(cul)
        if newcul != cul:
            print("newcul")
            for ix in range(9):
                grid[ix][sy] = newcul[ix]


def guess(current = True):
    global grid
    global gridlist
    global failed
    isvalid()
#    if current == True:
#        current = isvalid()
#   this is to be used when out of logic
#   gridlist  = []  and failed (number of failed "solutions")
#   are global variables for check
#   current = if current grid is viable
    if current == True:
        gridlist.append([[],[]])
        lastgrid = [["123456789" for i in range(9)] for i in range(9)]
        # save current grid
        cell = []
        for x in range(9):
            for y in range(9):
                lastgrid[x][y] = grid[x][y]
#                print(lastgrid)
#                input()

                if type(grid[x][y]) == str:
                    if len(cell) == 0:
                        cell = [grid[x][y],x,y]
                    else:
                        if len(grid[x][y]) < len(cell):
                            cell = [grid[x][y],x,y]
                            # pick a cell with fewest posibilities

        print(cell)
        if len(cell[0]) == 0: # if the shortest cell is without possibilities
            return guess(False) # grid not solvable, True was wrong
        grid[cell[1]][cell[2]] = int(cell[0][0])
        cell[0] = cell[0][1:]
        gridlist[-1] = [lastgrid,cell]
        print("gridlist -1 -1 ")
        print(gridlist[-1][-1])
    if current == False:
        failed +=1
        print(f"failed = {failed}")
        print(f"gridlist\n{gridlist}")
        print("gridlist[-1][-1]")
        print(gridlist[-1][-1])

        if len(gridlist[-1][-1][0]) == 0:
            gridlist = gridlist[:-1]
            return guess(False)
        cell = gridlist[-1][-1]
        print(f"cell = {cell}")
#        print("cell[0]")

#        print(cell[0])
        num = int(cell[0][0])
        cell[0] = cell[0][1:]
        print(f"num = {num}")
        grid[cell[1]][cell[2]] = num
        gridlist[-1][-1] = cell
        print(gridlist[-1])






        

    


def main():
    started = False
    initial_solve()
    step = 0
    stuck = 0
    solved = done()
    printgrid()
    #input()
    print("main")
    print(solved)
    valid = True
    while not solved:
        bckpgrid = [i for i in grid] # compare before and after solving
        if started == False:

            initial_solve()
            started = True
            valid = isvalid()

        sqr3()
        row()
        cul()
        sqr4()
        printgrid()
        if grid != bckpgrid:
            stuck = 0
            step+=1

            bckpgrid = [i for i in grid]
        else:
            stuck+=1
#        #input()
        if (step % 10 == 0 and step > 0 ) or (stuck % 10 == 0 and stuck > 0):
            print(f'step = {step}\nstuck = {stuck}')
            #input()

        if stuck > 1 and stuck % 10 == 0:
            guess()
        if len(gridlist) > 0:
            possible = isvalid()
            if not possible:
                guess(False)

        solved = done()
    if solved:
        valid = True
        for x in range(9):
            for y in range(9):
                if valid == True:
                    valid = finalcheck(grid[x][y],x,y)

        printgrid()
        print(valid)
        print(f'steps = {step}')
        if len(gridlist) > 0:
            for i in gridlist:
                print(i)
            print(f'gridlist len = {len(gridlist)}')

def main():
    initial_solve()
    while not done():
        for i in range(10):
            solveit()
            print()

        guess(isvalid())
        printgrid()
        print("{} gridlist".format(len(gridlist)))
    printgrid()


def getridofnone():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == None:
                grid[x][y] = "123456789"
def maintoo():
    getridofnone()
    count = 0
    isvalid()
    while not done():
#        cul()
#       row()
#        sqr3()
        guess(isvalid())
        count+=1
        print(count)
        if count % 1000 == 0:
            printgrid()
            print(failed)
            print(len(gridlist))
            input()
    printgrid()
    print(count)

if __name__ == "__main__":
#    grid = easy()
#    grid = medium()

    failed = 0
#    grid = hard()
#    grid = extreme()
    grid = hardest()
    gridlist= []
#    grid = hardest2()
    printgrid()
    main()
#    maintoo()
#    print(done())
