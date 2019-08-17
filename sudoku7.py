#define grid
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
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0 or grid[x][y] == None:
                grid[x][y] = "123456789"
    return cleanup(grid)

# clean from impossible numbers
def cleanup(grid):
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
                            diff = not (inrow and incul)
                            insqr = ((modx == modix) and (mody == modiy))
                            if diff and (inrow or incul or insqr):
                                grid[ix][iy] = grid[ix][iy].replace(num,"")
    return grid

# clen print
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
#            print(s)
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
            print(x,y,value)
            print(grid[x][y])
            printgrid()
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


if __name__ == "__main__":
#    grid = easy()
#    grid = medium()
#    grid = hard()
    grid = extreme()
#    grid = hardest()
#    grid = hardest2()
#    grid = newgrid()
#    printgrid(False)
#    grid = hardestinvalid()
#    grid = extremeinvalid()

    gridlist = []
    solve_by_guess()



