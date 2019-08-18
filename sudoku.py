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
# Other wise go to next cell
# Go to step 2


numbers = [i for i in range(1,10)]
grid = [[None for i in range(9)] for i in range(9)]

def checkrow(num,x):
    for i in grid[x]:
        if num == i:
            return False
    return True

def checkcolumn(num,y):
    for i in range(len(grid)):
        if grid[i][y] == num:
            return False
    return True

def checksquare(num,x,y):
    modx = int(x/3)*3
    mody = int(y/3)*3
    for row in range(modx,modx+3):
        for column in range(mody,mody+3):
            if grid[row][column] == num:
                return False
    return True


def givenumber(x,y):
    # if one possible ,return it as int
    # if more, return string of those
    numbers = []
    for i in range(1,10):
        if checksquare(i,x,y) == True:
            if checkcolumn(i,y) == True:
                if checkrow(i,x) == True:
                    numbers.append(i)
    if len(numbers) == 1:
        return numbers[0],True
    possible = ""
    for i in range(len(numbers)):
        possible += str(numbers[i])
#    print(f'possible numbers = {possible}')
#    input()

    return possible,False

def extremetry():
    grid = [['0' for i in range(9)] for i in range(9)]
    grid[0] = [0,0,9,0,3,0,0,0,8]
    grid[1] = [0,0,2,0,0,1,0,7,0]
    grid[2] = [0,0,0,6,7,0,0,4,0]
    grid[3] = [9,1,0,0,0,0,0,0,0]
    grid[4] = [0,6,7,0,0,0,8,5,0]
    grid[5] = [0,0,0,0,0,0,0,9,3]
    grid[6] = [0,9,0,0,8,6,0,0,0]
    grid[7] = [0,3,0,5,0,0,7,0,0]
    grid[8] = [8,0,0,0,1,0,2,0,0]
    for i in grid:
        print(i)
    for i in range(len(grid)):
        for s in range(len(grid[i])):
            if grid[i][s] == 0:
                grid[i][s] = '0'
    for i in grid:
        print(i)
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
    return grid

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

def done():
    for x in grid:
        for y in x:
            if type(y) == int:
                continue
            else:
                print(f'not done ! {y}')
                return False
    for x in range(len(grid)):
        modx = int(x/3)
        for y in range(len(grid[x])):
            mody = int(y/3)
            for ex in range(len(grid)):
                modex = int(ex/3)
                for wy in range(len(grid[ex])):
                    modwy = int(wy/3)
                    sqr = (modex == modx and modwy == mody)
                    row = (x == ex)
                    cul = (y == wy)
                    if sqr or row or cul:
                        if (x!= ex and y != wy):
                            if grid[x][y] == grid[ex][wy]:
                                print("{} is on {}{} and {}{}".format(
                                    grid[x][y],x,y,ex,wy))
                                print("error")
                                
                                return True


    for row in grid:
        print(row)
    print("DONE!")
    return True

def printgrid():
    for i in grid:
        print(i)
    input()

def uniquesteptwo(num,x,y):
    modx = int(x/3)
    mody = int(y/3)
    for ex in range(len(grid)):
        modex = int(ex/3)
        for wy in range(len(grid[ex])):
            modwy = int(ex/3)
            if not (x == ex and y == wy):
                sqr = (modex == modx and modwy == mody)
                row = (x == ex)
                cul = (y == wy)

                if sqr or row or cul:
                    if type(grid[ex][wy]) == int:
                        if grid[ex][wy] == num:
                            return False
                    else:
                        for n in grid[ex][wy]:
                            if int(n) == num:
                                return False

    return True

def steptwochecking(x,y):
    pn = [int(i) for i in grid[x][y]]
    for i in pn:
        if uniquesteptwo(i,x,y) == True:
            return i
#        if uniqueinrow(i,x,y) == True:
#            print(f"uir {i} = {x},{y}")
#            return i
#        if uniqueinsquare(i,x,y) == True:
#            print("uis")
#            return i
#        if uniqueinculomn(i,x,y) == True:
#            print(f"uic {i} = {x},{y}")
#            return i

    return grid[x][y]

def steptwo(): # if simple logic is not enough
    progress = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            s = grid[x][y]
            if type(grid[x][y]) != int:
                grid[x][y] = steptwochecking(x,y)
            if s != grid [x][y]:
                progress = True


    return progress

def stepone():
    progress = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) != int:
                grid[x][y],check = givenumber(x,y)
                if progress == False and check == True:
                    progress = True
    return progress


def main():

    global grid
#    grid = hardtry()
    grid = extremetry()

#    grid = basictry()
    for i in grid:
        print(i)
    step = 1
    while not done():
        if not stepone():
            print(f'step {step}')
            step+=1
#            print(f'progress = {progress}')
            if not steptwo():
                print("st")
        printgrid()


if __name__ == "__main__":
    main()
