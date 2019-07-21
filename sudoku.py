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

import random

numbers = [i for i in range(1,10)]
grid = [[None for i in range(9)] for i in range(9)]

def checkrow(num,x):
    if num in grid[x]:
        return False
    return True

def checkcolumn(num,y):
    for i in range(len(grid)):
        if num == grid[i][y]:
            return False
    return True


def checksquare(num,x,y):
    modx = int(x/3)*3 

    mody = int(y/3) *3
#    print(f'{x} = {modx}')
#    print(f'{y} = {mody}')
    for rowx in range(modx,modx+3):
        for culomny in range(mody,mody+3):
            if num == grid[rowx][culomny]:
                return False
    return True



def givecellnumber(x,y):
    tries = 0
    while True:
        tries += 1
        r= random.randint(0,8)

        numtry = numbers[r]
        if checksquare(numtry,x,y) == True:
            if checkcolumn(numtry,y) == True:
                if checkrow(numtry,x) == True:
                    return numtry
        
        if tries > 100:
            for line in grid:
                print(line)
            input()


    return numtry

def basictry():
    grid = [[0 for i in range(9)] for i in range(9)]
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
            if type(y) == int and y > 0:
                continue
            else:
                print(f'not done ! {y}')
                return False
    return True
if __name__ == "__main__":
    grid = basictry()
    for i in grid:
        print(i)
    input()
    for row in range(len(grid)):
        for cell in range(len(grid)):
            r = random.randint(0,8)
            if grid[row][cell] == 0:

                grid[row][cell] = givecellnumber(row,cell)
                print('grid[row][cell] = {}'.format(grid[row][cell]))
                done()
    print(done())
    for line in grid:
        print(line)
