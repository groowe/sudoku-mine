

def basictry():
        grid = [['0' for i in range(9)] for i in range(9)]
        grid[0][0] = 5
        grid[0][1] = 3
        grid[0][4] = 7
        grid[1][0] = 6
        grid[1][3] = 1
        grid[1][4] = 9
        grid[1][5] = 5
        grid[2][1] = 9
        grid[2][2] = 8
        grid[2][7] = 6
        grid[3][0] = 8
        grid[3][4] = 6
        grid[3][8] = 3
        grid[4][0] = 4
        grid[4][3] = 8
        grid[4][5] = 3
        grid[4][8] = 1
        grid[5][0] = 7
        grid[5][4] = 2
        grid[5][8] = 6
        grid[6][1] = 6
        grid[6][6] = 2
        grid[6][7] = 8
        grid[7][3] = 4
        grid[7][4] = 1
        grid[7][5] = 9
        grid[7][8] = 5
        grid[8][4] = 8
        grid[8][7] = 7
        grid[8][8] = 9
        return grid


def build_grid():
    return basictry()


def printgrid():
    for i in grid:
        print(i)
    input()

def basicnum():
    progress = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) == str:
                modx = int(x/3)
                mody = int(y/3)
                poss = "123456789"
                for xs in range(len(grid)):
                    modxs = int(xs/3)
                    for ys in range(len(grid[xs])):
                        modys = int(ys/3)
                        sqr = ((modys == mody) and (modx == modxs))
                        line = (x == xs)
                        row = (y == ys)
                        same =( (x == xs) and (y == ys))
#                        print(f"x,y {x},{y}\n xs,ys {xs},{ys}")
#                        print(f"line {line}\nrow {row}\n sqr {sqr}")
                        if (row == True or line == True or sqr == True):
                            if not same:

                                if type(grid[xs][ys]) == int:
                                    poss = poss.replace(str(grid[xs][ys]),"")
#                                    print(poss)
                if len(poss) == 1:
                    grid[x][y] = int(poss)
                    progress = True
                elif len(poss) == 0:
                    print("Error in basicnum\nwhaaaaaaaat?")
                    printgrid()
                    print(f"{x}{y} {grid[x][y]} poss = {poss}")

                    quit()
                elif len(poss) > 1:
#                    print(type(grid[x][y]))
                    if grid[x][y]== '0' or len(grid[x][y]) > len(poss):
                        grid[x][y] = poss
                        progress = True
                        print(f'progress')
#                print(poss)
    return progress
def clear(itemlist):
    for item in itemlist:
        if type(item) == int:
            for i in range(len(itemlist)):
                if type(itemlist[i]) == str:

                    if str(item) in itemlist[i]:
                        itemlist[i] = itemlist[i].replace(str(item),"")
                        if len(itemlist[i]) == 1:
                            itemlist[i] = int(itemlist[i])
    return itemlist


def solvesqr(sqr,modx,mody):
    # if num only in one row / culomn , clear other instances
    # in row / culomn outside of sqr

    # if 2 nums occupy 2 places , clear other nums from those places
    # if 3 nums ...
    # if 4 nums ...

    # TBD

    pass

def solverow(row):
#    print("solverow")
    row = clear(row)
    oldrow = [i for i in row]
#    print(row)

    for item in range(len(row)):
        if type(row[item]) == str:
            for num in row[item]:
                unique = True
                for it in range(len(row)):
                    if it != item:
                        if type(row[it]) == str:
                            if num in row[it]:
                                unique = False
                if unique == True:
                    row[item] = int(num)
 
    if oldrow != row:
        printgrid()
#        print(oldrow)
#        print(row)
#        input()
    return row




def solve():
#    print("solve")
    
    # rows
    for x in range(len(grid)):
#        print("solve to row")
        grid[x] = solverow(grid[x])
    # culomn
    for y in range(len(grid)):
        cull = []
        for x in range(len(grid)):
            cull.append(grid[x][y])
        cull = solverow(cull)
        for x in range(len(grid)):
            grid[x][y] = cull[x]
    sqr = [[[] for i in range(3)] for i in range(3)]
    for x in range(len(grid)):
        modx = int(x/3)
        for y in range(len(grid[x])):
            mody = int(y/3)
            sqr[modx][mody].append(grid[x][y])
    print("sqr")
    for x in range(len(sqr)):
        for y in range(len(sqr[x])):
            solvesqr(sqr[x][y],x,y)
#            print(sqr[x][y])
    input()





def newtry2():
    grid = [['0' for i in range(9)] for i in range(9)]

    grid[0] = [0,4,0,0,0,8,0,0,0]
    grid[1] = [0,0,8,0,0,0,6,7,0]
    grid[2] = [0,9,0,0,2,0,0,0,0]
    grid[3] = [9,0,0,8,0,0,4,0,2]
    grid[4] = [0,2,0,7,0,4,0,3,0]
    grid[5] = [1,0,4,0,0,3,0,0,5]
    grid[6] = [0,0,0,0,6,0,0,5,0]
    grid[7] = [0,5,9,0,0,0,1,0,0]
    grid[8] = [0,0,0,3,0,0,0,2,0]
    for i in grid:
        print(i)
        for i in range(len(grid)):
            for s in range(len(grid[i])):
                if grid[i][s] == 0:
                    grid[i][s] = '123456789'
    return grid

def newtry3():
    grid = [['0' for i in range(9)] for i in range(9)]

    grid[0] = [0,0,0,0,0,0,2,9,0]
    grid[1] = [2,1,0,4,0,3,0,0,0]
    grid[2] = [3,0,0,0,5,2,0,0,0]
    grid[3] = [0,0,5,0,0,0,0,6,0]
    grid[4] = [0,7,0,6,0,8,0,4,0]
    grid[5] = [0,8,0,0,0,0,7,0,0]
    grid[6] = [0,0,0,7,6,0,0,0,8]
    grid[7] = [0,0,0,8,0,1,0,3,4]
    grid[8] = [0,4,1,0,0,0,0,0,0]
    for i in grid:
        print(i)
        for i in range(len(grid)):
            for s in range(len(grid[i])):
                if grid[i][s] == 0:
                    grid[i][s] = '123456789'
    return grid

def newtry():
    grid = [['0' for i in range(9)] for i in range(9)]

    grid[0] = [0,0,0,0,5,0,4,0,0]
    grid[1] = [8,0,0,0,0,3,5,0,0]
    grid[2] = [0,0,0,0,0,2,8,9,0]
    grid[3] = [6,0,5,0,0,1,0,0,0]
    grid[4] = [0,1,0,4,0,9,0,3,0]
    grid[5] = [0,0,0,6,0,0,1,0,8]
    grid[6] = [0,8,6,1,0,0,0,0,0]
    grid[7] = [0,0,2,3,0,0,0,0,9]
    grid[8] = [0,0,4,0,9,0,0,0,0]
    for i in grid:
        print(i)
        for i in range(len(grid)):
            for s in range(len(grid[i])):
                if grid[i][s] == 0:
                    grid[i][s] = '123456789'
    return grid

def newtry():
    grid = [['0' for i in range(9)] for i in range(9)]

    grid[0] = [0,0,0,0,5,0,4,0,0]
    grid[1] = [8,0,0,0,0,3,5,0,0]
    grid[2] = [0,0,0,0,0,2,8,9,0]
    grid[3] = [6,0,5,0,0,1,0,0,0]
    grid[4] = [0,1,0,4,0,9,0,3,0]
    grid[5] = [0,0,0,6,0,0,1,0,8]
    grid[6] = [0,8,6,1,0,0,0,0,0]
    grid[7] = [0,0,2,3,0,0,0,0,9]
    grid[8] = [0,0,4,0,9,0,0,0,0]
    for i in grid:
        print(i)
        for i in range(len(grid)):
            for s in range(len(grid[i])):
                if grid[i][s] == 0:
                    grid[i][s] = '123456789'
    return grid

def newtry():
    grid = [['0' for i in range(9)] for i in range(9)]

    grid[0] = [0,0,0,0,5,0,4,0,0]
    grid[1] = [8,0,0,0,0,3,5,0,0]
    grid[2] = [0,0,0,0,0,2,8,9,0]
    grid[3] = [6,0,5,0,0,1,0,0,0]
    grid[4] = [0,1,0,4,0,9,0,3,0]
    grid[5] = [0,0,0,6,0,0,1,0,8]
    grid[6] = [0,8,6,1,0,0,0,0,0]
    grid[7] = [0,0,2,3,0,0,0,0,9]
    grid[8] = [0,0,4,0,9,0,0,0,0]
    for i in grid:
        print(i)
        for i in range(len(grid)):
            for s in range(len(grid[i])):
                if grid[i][s] == 0:
                    grid[i][s] = '123456789'
    return grid
def hardtry():
    grid = [['0' for i in range(9)] for i in range(9)]
    grid[0] = [3,0,0,2,0,0,1,0,0]
    grid[1] = [0,0,5,7,1,3,0,0,0]
    grid[2] = [0,0,7,4,6,0,8,0,0]
    grid[3] = [8,0,0,3,0,0,0,1,2]
    grid[4] = [7,0,0,8,5,0,0,0,9]
    grid[5] = [9,2,0,0,4,6,0,0,0]
    grid[6] = [0,7,0,0,0,0,0,4,6]
    grid[7] = [0,1,0,0,0,0,2,5,8]
    grid[8] = [0,0,0,5,0,4,0,9,0]
    for i in grid:
        print(i)
        for i in range(len(grid)):
            for s in range(len(grid[i])):
                if grid[i][s] == 0:
                    grid[i][s] = '0'
    for i in grid:
        print(i)
    print("hardtry")
    return grid

def done():
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) == str:
                return False
    return True

def main():
#    printgrid()
    basicnum()
    while not done():
        progress = True
        while progress:
            progress = basicnum()
            printgrid()
            print(f'main progress {progress}')
        solve()
        print("harder")
        printgrid()
    printgrid()
    print("DONE")


if __name__ == "__main__":
#    grid = build_grid()
#    grid = hardtry()
#    grid = newtry()
#    grid = newtry2()
    grid = newtry3()
    main()
