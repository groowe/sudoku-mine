# level 0 ways
# functions here :
# from level0 import Cleanup,Naked_Single,Unique
def Cleanup(grid):
    found = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) == int:
                modx = int(x/3)
                mody= int(y/3)
                num =str(grid[x][y])
                for xx in range(9):
                    modxx = int(xx/3)
                    inrow = (xx == x)

                    for yy in range(9):
                        if type(grid[xx][yy]) == str:
                            modyy = int(yy/3)
                            incol = (yy == y)
                            numin = (num in grid[xx][yy])
                            insqr = ((modx == modxx) and (mody == modyy))
                            diff = not(inrow and incol)
                            if (insqr or inrow or incol) and diff and numin:
                                found = True
#                                print(grid[xx][yy])
                                grid[xx][yy] = grid[xx][yy].replace(num,'')

#                                print(grid[xx][yy])
    return [grid,found]

def Naked_Single(grid):
    found = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if type(grid[x][y]) == str:
                if len(grid[x][y]) == 1:
                    grid[x][y] = int(grid[x][y])
                    found = True
    return [Cleanup(grid)[0],found]

    
def Unique(unit):
    found = False
    for i in range(1,10):
        count = 0
        index = None
        for cell in range(len(unit)):
            if type(unit[cell]) == str:
                if str(i) in unit[cell]:
                    count+=1
                    if count == 1:
                        index = cell
        if count == 1:
            unit[index] = i
            found = True
    return [unit,found]
#NOTE this next one will need to be more general
####################################################################
#def Uniques(grid):
#    found = False
#    for x in range(9):
#        row = Unique(grid[x])
#        if row[1]:
#            grid[x] = row[0]
#            found = True
#        column = []
#        for s in range(9):
#            column.append(grid[s][x])
#        column = Unique(column)
#        if column[1]:
#            found = True
#            for s in range(9):
#                grid[s][x] = column[0][s]
#    for modx in range(3):
#        for mody in range(3):
#            sqr = []
#            for x in range(modx*3,(modx+1)*3):
#                for y in range(mody*3,(mody+1)*3):
#                    sqr.append(grid[x][y])
#            sqr  = Unique(sqr)
#            if sqr[1]:
#                found = True
#                ind = 0
#                for x in range(modx*3,(modx+1)*3):
#                    for y in range(mody*3,(mody+1)*3):
#                        grid[x][y] = sqr[0][ind]
#                        ind+=1
#
#    return [Cleanup(grid)[0],found]

#if __name__ == "__main__":
#    import unittest
#    
#    class TestStringMethods(unittest.TestCase))
#
