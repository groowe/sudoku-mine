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
            if grid[x][y] == None or grid[x][y] == 0:
                return False
            if type(grid[x][y]) == str:
                return False
    return True


def clearnei(num,x,y):
    modx = int(x/3)
    mody = int(y/3)
    for a in range(9):
        moda = int(a/3)
        for b in range(9):
            modb = int(b/3)
            sqr = ((modx == moda) and (mody == modb))
            line = (x == a)
            culomn = (y == b)
            diff  = not ((x == a) and (y == b))
            st = (type(grid[a][b]) == str)
            act = ((sqr or line or culomn) and diff and st)
#            act = (line and diff and st)
            if act == True:
#                print(act)
                grid[a][b] = grid[a][b].replace(str(num),"")
                if len(grid[a][b]) == 1:
                    if setu(grid[a][b],a,b) == True:

                        grid[a][b] = int(grid[a][b])
                    else:
                        print(f'{x}{y}  {a}{b}  {num}')
                        printgrid()
                        quit()





def initial_solve():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == None:
                grid[x][y] = "123456789"
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == int:
                clearnei(grid[x][y],x,y)
    row()
    culomn()
    sqr()


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
                    if un == True:
                        if setu(n,x,y) == True:
                            grid[x][y] = int(n)

                            clearnei(grid[x][y],x,y)
                        if check() == False:
                            print(f'{x}{y} - {i}')
                            printgrid()
                            quit()


def setu(num,x,y):
    if type(num) == str:
        if len(num ) > 1:
            return False
        num = int(num)




    modx = int(x/3)
    mody = int(y/3)
    for a in range(9):
        moda = int(a/3)
        for b in range(9):
            modb = int(b/3)
            sqr = ((modx == moda) and (mody == modb))
            line = (x == a)
            culomn = (y == b)
            diff  = not ((x == a) and (y == b))
            st = (type(grid[a][b]) == int)
            act = ((sqr or line or culomn) and diff and st)
            if act and grid[a][b] == num:
                print(f'{num} cannot be at {x}{y}')
                print(f'it is at {a}{b} already')
                printgrid()
                input()
                return False
    return True

def culomn():
    for y in range(9):
        for x in range(9):
            if type(grid[x][y]) == str:
                for n in grid[x][y]:
                    un = True
                    for ex in range(9):
                        if ex != x:
                            if type(grid[ex][y]) == str:
                                if n in grid[ex][y]:
                                    un = False
                    if un == True:
                        if setu(grid[x][y],x,y) == True:

                            grid[x][y] = int(n)
                            clearnei(grid[x][y],x,y)

def sqr():
    for x in range(9):
        modx = int(x/3)
        for y in range(9):
            mody = int(y/3)
            if type(grid[x][y]) == str:
                for n in grid[x][y]:
                    un = True
                    for a in range(modx*3,(modx*3)+3):
                        for b in range(mody*3,(mody*3)+3):
                            diff = not( (x == a) and (y == b))
                            i = (type(grid[a][b]) == int)
                            s = (type(grid[a][b]) == str)
                            if diff == True:
                                if i == True:
                                    if grid[a][b] == int(n):
                                        grid[x][y] == grid[x][y].replace(n,"")
                                if s == True:
                                    if n in grid[a][b]:
                                        un = False
                    if un == True:
                        if setu(grid[x][y],x,y) == True:
                            grid[x][y] = int(n)




def sqr2():
    modx = 0
    mody = 0
    while mody < 3:
        sqr = []
        for x in range(modx*3,(modx*3)+3):
            for y in range(mody*3,(mody*3)+3):
                sqr.append(grid[x][y])
        
        for item in range(len(sqr)):
            if type(sqr(item)) == str:
                cul = item % 3      # 0 1 2 0 1 2 0 1 2
                row = int(item / 3) # 0 0 0 1 1 1 2 2 2
                onlycul = True
                onlyrow = True
                for n in sqr(item):
                    for i in range(len(sqr)):
                        if i != item:
                            if type(sqr(i)) == str:
                                if n in sqr[i]:
                                    culi = i %3
                                    rowi = int(i/3)
                                    if culi != cul:
                                        onlycul = False
                                    if rowi != row:
                                        onlyrow = False
                if onlyrow == True:
                    s = (mody*3) + row
                    for i in range(9):
                        # TBD
                        if type(grid[s][i])



        if modx == 2:
            mody+=1
            modx = 0
        else:
            modx += 1




def check():
    for x in range(9):
        for y in range(9):
            if type(grid[x][y] ) == int:
                n = grid[x][y]
                modx = int(x/3)
                mody = int(y/3)
                for a in range(9):
                    moda = int(a/3)
                    for b in range(9):
                        modb = int(b/3)
                        row = (a == x)
                        culomn = (b ==y)
                        sqr = ((modx == moda) and (mody == modb))
                        diff = not ((x == a) and (y == b))
                        if (row or culomn or sqr) and diff:
                            if grid[a][b] == n:
                                print(f'{x}{y} {a}{b} {n}')
                                return False
    return True


def main():
    step = 0
    while not done():

        initial_solve()
        printgrid()
        if check()== False: # aaaaaaaaaaa .... 
            print("error")
        step +=1
        if step % 10 == 0:
            print(step)
            input()
if __name__ == "__main__":
#    grid = easy()
#    grid = medium()
    grid = hard()
#    grid = extreme()
    printgrid()
    main()
#    print(done())
