# all level1 techniques 
# functions here : 
# from level1 import Naked_Pair,Hidden_Pair,Box_Line,Pointing_Line
def Naked_Pair(unit):
    found = False
    for x in range(len(unit)):
        if type(unit[x]) == str:
            if len(unit[x]) == 2 and unit.count(unit[x]) == 2:
                indexes = [i for i in range(len(unit)) if unit[i] == unit[x]]
                nums = unit[x]
                for n in nums:
                    for i in range(len(unit)):
                        if i not in indexes:
                            if type(unit[i]) == str and n in unit[i]:
                                found= True
                                unit[i] = unit[i].replace(n,'')
    return [unit,found]


def Hidden_Pair(unit):
    found = False

    nums = [None] # for 0
    for i in range(1,10):
        s = []
        for ind in range(len(unit)):
            if type(unit[ind]) == str and str(i) in unit[ind]:
                s.append(ind)
        nums.append(s) # index of nums == i ,  nums[i] == index in unit
    done = []
    for n in nums:
        if n != None and len(n) == 2 and nums.count(n) == 2 and n not in done:
            nms = [i for i in range(len(nums)) if nums[i] == n]
            nms = str(nms[0])+str(nms[1])
            for ind in n:
                unit[ind] = nms
                done.append(ind)
                found = True
    return [unit,found]

def Box_Line(grid):
    found = False
    for x in range(len(grid)):
        for num in range(1,10):
            num = str(num)
            line = [i for i in range(9) if (type(grid[x][i]) == str and num in grid[x][i])]
            coll = [i for i in range(9) if (type(grid[i][x]) == str and num in grid[i][x])]
            modline = (len(set([int(i/3) for i in line])) == 1)
            modcoll = (len(set([int(i/3) for i in coll])) == 1)
            if (modline or modcoll):
                if modline:
                    modx = int(x/3)
                    mody= int(line[0]/3)
                    orig = [[x,y] for y in line]
                else:
                    modx = int(coll[0]/3)
                    mody = int(x/3)
                    orig = [[y,x] for y in coll]

                for xx in range(len(grid)):
                    modxx = int(xx/3)
                    if modx == modxx:
                        for yy in range(len(grid[xx])):
                            modyy = int(yy/3)
                            if mody == modyy:
                                if [xx,yy] not in orig:
                                    if type(grid[xx][yy]) == str and num in grid[xx][yy]:
                                        found = True
                                        grid[xx][yy] = grid[xx][yy].replace(num,'')
    return [grid,found]


def Pointing_Line(grid):
    found = False

    for modx in range(3):
        for mody in range(3):
            sqr = []
            for x in range(modx*3,(modx+1)*3):
                for y in range(mody*3,(mody+1)*3):
                    sqr.append(grid[x][y])
            for num in range(1,10):
                num = str(num)
                row = []
                col = []
                for s in range(len(sqr)):
                    if type(sqr[s]) == str and num in sqr[s]:
                        row.append(int(s/3))
                        col.append(s%3)
                inrow = (len(set(row)) == 1)
                incol = (len(set(col)) == 1)

                if (inrow or incol) :
                    if inrow:
                        stat = row[0] + (modx*3)
                        coords = [[stat,yy] for yy in range(9) if int(yy/3) != mody]
                    else:

                        stat = row[0] + (mody*3)
                        coords = [[yy,stat] for yy in range(9) if int(yy/3) != modx]
                    for c in coords:
                        if type(grid[c[0]][c[1]]) == str and num in grid[c[0]][c[1]]:
                            grid[c[0]][c[1]] = grid[c[0]][c[1]].replace(num,'')
                            found = True
    return [grid,found]

