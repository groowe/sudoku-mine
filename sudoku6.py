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



def gridinit(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == None:
                grid[x][y] = "123456789"
                modx = int(x/3)
                mody = int(y/3)
                for ex in range(9):
                    for ey in range(9):
                        if type(grid[ex][ey]) == int:
                            num = str(grid[ex][ey])
                            modex = int(ex/3)
                            modey = int(ey/3)

                            same =( (x == ex) and (y == ey))
                            insqr = ((modx == modex) and (modey == mody))
                            inrow = (x == ex)
                            incul = (y == ey)
                            if not same:
                                if insqr or inrow or incul:
                                    grid[x][y] = grid[x][y].replace(num,"")
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

def printgrid(filtered=True):
    print("_"*27)
    if filtered == True:

        for x in range(len(grid)):
#        print('x')
#        print(x)
            if x > 0 and x % 3 == 0:
                print("_"*27)
            s = preprint(grid[x])
#        print(len(s))
            print("{}".format(s))
        print("_"*27)
    else:
        for x in range(len(grid)):
            print(grid[x])

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



def solve():
    progress = False
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                if len(grid[x][y]) == 1:
                    grid[x][y] = int(grid[x][y])
                    printgrid()
                    progress = True
#    if progress == True:
#        return solve()
    print(""" row by row""")
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                for i in range(9):
                    if i != y:
                        if type(grid[x][i]) == int:
                            s = str(grid[x][i])
                            grid[x][y] = grid[x][y].replace(s,"")
                if len(grid[x][y]) == 1:
                    n = int(grid[x][y])

                    progress = setnum(n,x,y)
 #   if progress == True:
 #       return solve()
    print(""" culomn by culomn """)
    for y in range(9):
        for x in range(9):
            if type(grid[x][y]) == str:
                for ex in range(9):
                    if ex != x:
                        if type(grid[ex][i]) == int:
                            s = str(grid[ex][i])
                            grid[x][y] = grid[x][y].replace(s,"")
                if len(grid[x][y]) == 1:
                    n = int(grid[x][y])
                    progress = setnum(n,x,y)
#    if progress == True:
#        return solve()

    print(""" sqr by sqr """)
    modx = 0
    mody = 0
    while modx < 3:
        for x in range(modx*3,(modx*3)+3):
            for y in range(mody*3,(mody*3)+3):
                if type(grid[x][y]) == str:
                    for ex in range(modx*3,(modx*3)+3):
                        for ey in range(mody*3,(mody*3)+3):
                            same = ((x == ex) and (y == ey))
                            if not same:
                                if type(grid[ex][ey]) == int:
                                    s = str(grid[ex][ey])
                                    grid[x][y] = grid[x][y].replace(s,"")
                    if len(grid[x][y]) == 1:
                        n = int(grid[x][y])
                        progress = setnum(n,x,y)


        if mody == 2:
            modx +=1
            mody = 0
        else:
            mody +=1
    if progress == True:
        printgrid()
        input()
 
    return progress
"""
    if progress == True:
        return solve()



    if done():
        printgrid()
        print("DONE")
        quit()




    return solve()

"""

def setnum(num,x,y):
    if type(num) != int:
        num = int(num)
    modx = int(x/3)
    mody = int(y/3)
    for ex in range(9):
        modex = int(ex/3)
        for ey in range(9):
            modey = int(ey/3)
            insqr = ((modx == modex)and (modey == mody))
            inrow = (x == ex)
            incul = (y == ey)
            dif = not (inrow and incul)
            if dif and (insqr or inrow or incul):
                if grid[ex][ey] == num or grid[ex][ey] == str(num):
                    print(False)
                    return False
    grid[x][y] = num
    return True
                        

if __name__ == "__main__":
    grid = easy()
    grid = gridinit(grid)

    printgrid(False)
    count = 0
    while True:
        solve()
        count+=1
        if count > 20:
            if count % 10 == 0:
                printgrid()
                input()
                printgrid(False)
                input()

