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

def preprint(line):
    s = str(line)
    s = s.replace("None"," ").replace("[","|")
    s = s.replace("]","|")
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
    return True



def initial_solve():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == None or grid[x][y] == 0:
                grid[x][y] = "123456789"
    printgrid()

#    input("initialsolve")
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == int:

                clearnei(grid[x][y],x,y)
    printgrid()
#    input("aftersolve")


def clearnei(fromnum,x,y):
    print("clearnei")
    print(fromnum,x,y)
    divx = int(x/3)
    divy = int(y/3) # defining square
    if type(fromnum) == int:
        fromnum = str(fromnum)
    for ex in range(9):
        divex = int(ex/3)
        for ey in range(9):
            divey = int(ey/3)
            insqr = ((divx == divex) and (divy == divey))
            inrow = (y == ey)
            incul = (x == ex)
            difstr = (not((x == ex) and (y == ey)) and type(grid[ex][ey]) == str)

            if difstr and (insqr or inrow or incul):
                if fromnum in grid[ex][ey]:
                    grid[ex][ey] = grid[ex][ey].replace(fromnum,"")
                    if len(grid[ex][ey]) == 1:
                            grid[ex][ey] = int(grid[ex][ey])
                            clearnei(grid[ex][ey],ex,ey)



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
#        input()

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
#                input()
#            else:
#                print(False)
#                printgrid()
#                input("ERRRRRRRRRRRRR")
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
                                else:
                                    print(f'cula = {cula},culnum = {culnum}')
                                if cula != culnum:
                                    uniqueincul = False
                        
                    x = rownum + (modx*3)
                    y = culnum + (mody*3)
#                    print(f'num = {num}, x,y = {x},{y}\nrowunique = {uniqueinrow},culunique = {uniqueincul}')
                    if uniqueinrow or uniqueincul:
#                        print(sqr)
                        printgrid()
#                        input()

                    if uniqueinrow == True:
                        for sy in range(9):
                            modsy = int(sy/3)
                            if modsy != mody:
                                if type(grid[x][sy]) == str:
                                    grid[x][sy] = grid[x][sy].replace(num,"")
                                    if len(grid[x][sy]) == 1:

                                        grid[x][sy] = int(grid[x][sy])
                                        clearnei(grid[x][sy],x,sy)
                                        return sqr3()
                    elif uniqueincul == True:
                        for sx in range(9):
                            modsx = int(sx/3)
                            if modsx != modx:
                                if type(grid[sx][y]) == str:
                                    grid[sx][y] = grid[sx][y].replace(num,"")

                                    if len(grid[sx][y]) == 1:
                                        grid[sx][y] = int(grid[sx][y])
                                        clearnei(grid[sx][y],sx,y)
                                        return sqr3()



        if mody ==2:
            mody = 0
            modx +=1
        else:
            mody +=1
#        print(modx,mody)
#        print("sqr")
#        printgrid()
#        input()


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
                                    grid[x][y] = grid[x][y].replace(n,"")
                                    un = False
                    if un == True:
                        if type(grid[x][y]) == str:

                            grid[x][y] = int(n)
                            clearnei(int(n),x,y)



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
                                        input()
                                        un = False
                                    else:
                                        grid[x][y] = grid[x][y].replace(n,"")
                    if un == True:
                        grid[x][y] = int(n)
                        clearnei(int(n),x,y)


def main():
    started = False
    initial_solve()
    step = 0
    solved = done()
    print("main")
    print(solved)
    while not solved:
        if started == False:

            initial_solve()
            started = True
        sqr3()
        row()
        cul()
        printgrid()
        step +=1
#        input()
        solved = done()
        if step % 10 == 0:
            print(step)
            input()
    if solved:
        valid = True
        for x in range(9):
            for y in range(9):
                if valid == True:
                    valid = finalcheck(grid[x][y],x,y)

        printgrid()
        print(valid)
        print(f'steps = {step}')




if __name__ == "__main__":
#    grid = easy()
#    grid = medium()
#    grid = hard()
    grid = extreme()
    printgrid()
    main()
#    print(done())
