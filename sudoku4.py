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

def printgrid():
    for x in range(len(grid)):
        print(grid[x])

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
            same = ((x == a) and (y == b))
            diff = not same
            st = (type(grid[a][b]) == str)
            act = ((sqr or line or culomn) and diff and st)
#            act = (line and diff and st)
            if act == True:
#                print(act)
                grid[a][b] = grid[a][b].replace(str(num),"")
                if len(grid[a][b]) == 1:
                        grid[a][b] = int(grid[a][b])





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
                        grid[x][y] = int(n)

                        clearnei(grid[x][y],x,y)
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
                    for ex in range(9):
                        modex = int(ex/3)
                        for yp in range(9):
                            modyp = int(yp/3)
                            sq = ((modx == modex) and (mody == modyp))
                            dif = not ((x == ex) and (y == yp))
                            st = (type(grid[ex][yp]) == str) 
                            if sq and dif and st:
                                if n in grid[ex][yp]:
                                    un = False
                    if un == True:
                        grid[x][y] = int(n)


                        clearnei(grid[x][y],x,y)

def main():
    while not done():

        initial_solve()
        printgrid()
        input()
if __name__ == "__main__":
    grid = easy()
#    grid = medium()
#    grid = hard()
#    grid = extreme()
    printgrid()
    main()
#    print(done())
