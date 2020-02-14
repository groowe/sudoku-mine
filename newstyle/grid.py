from level0 import Cleanup
from copy import deepcopy as dc
def basicgrid():
    return [['123456789' for i in range(9)] for i in range(9)]

def standardize(grid):
    gg = []
    for x in range(len(grid)):
        gg.append([])
        for y in range(len(grid[x])):
            gg[x].append([])
            if grid[x][y] == None or grid[x][y] == 0 or grid[x][y] == '0':
#                grid[x][y] == "123456789"
                gg[x][y] = '123456789'
            elif type(grid[x][y]) == str and len(grid[x][y]) == 1:
                gg[x][y] = int(grid[x][y])
            else:
                gg[x][y] = grid[x][y]


    return Cleanup(gg)[0]

def done(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) == str:
                return False,False
    return True, validate_solution(grid)

def validate_solution(grid):
    nums = [i for i in range(1,10)]
    for num in nums:
        ind = [i for i in range(9)]
        for x in range(len(grid)):
            if grid[x].count(num) != 1:
                return False
            try:
                ind.remove(grid[x].index(num))
            except ValueError:
                return False
            except Exception as ex:
                print('validate_solution unexpected exception:')
                print(f'**'*31)
                print(f'exception = {ex}\nx = {x} num = {num}')
                print(f'grid:\n{grid}')
                print('eof'+'**'*30)


def copyofgrid(grid):
    return dc(grid)

################ some pregenareted sudokus #####################

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

# some invalid sudokus:

def hardestinvalid():
    grid  = hardest()
    grid[8][8] = 3
    return grid

def extremeinvalid():
    grid = extreme()
    grid[4][4] = 6
    return grid

###############################################################
